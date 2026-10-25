#!/usr/bin/env python3
"""Local conditional lesson store: immutable revisions and an atomic compact index."""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import sys

if not sys.platform.startswith('linux'):
    raise SystemExit('Contextual learning is Linux-only; no lesson files were read or written.')

import fcntl
import tempfile

ROOT = Path(os.environ.get('CODEX_HOME') or Path.home() / '.codex').expanduser() / 'learning'
STATUSES = {'candidate', 'verified', 'attributed-feedback', 'superseded'}
KINDS = {'application-bug', 'agent-mistake', 'tool-limitation', 'transient-failure', 'permission-denial'}
FIELDS = {'id', 'title', 'status', 'failure_kind', 'keywords', 'problem', 'causal_principle', 'origin', 'context', 'applicability', 'exclusions', 'diagnostic_checks', 'correction', 'invariants', 'verification', 'source', 'conflicts_with', 'supersedes', 'superseded_by', 'status_reason'}


def encoded(value):
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + '\n').encode()


def digest(value):
    return hashlib.sha256(encoded(value)).hexdigest()


def identifier(value):
    if not isinstance(value, str) or not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,95}', value):
        raise ValueError('invalid lesson ID')
    return value


def nonempty(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{label} must be nonempty text')


def strings(value, label, required=True):
    if not isinstance(value, list) or (required and not value):
        raise ValueError(f'{label} must be a list' + (' with entries' if required else ''))
    for entry in value:
        nonempty(entry, label)


def facts(value, label):
    if not isinstance(value, dict) or not value:
        raise ValueError(f'{label} must be a nonempty fact map')
    for key, entry in value.items():
        nonempty(key, label)
        nonempty(entry, label)


def validate(lesson):
    if not isinstance(lesson, dict) or set(lesson) != FIELDS:
        raise ValueError('lesson must contain exactly the fields in lesson-template.json')
    identifier(lesson['id'])
    if lesson['status'] not in STATUSES or lesson['failure_kind'] not in KINDS:
        raise ValueError('invalid status or failure_kind')
    for field in ['title', 'problem', 'causal_principle', 'status_reason']:
        nonempty(lesson[field], field)
    for field in ['keywords', 'diagnostic_checks', 'invariants']:
        strings(lesson[field], field)
    for field in ['conflicts_with', 'supersedes', 'superseded_by']:
        strings(lesson[field], field, False)
        for entry in lesson[field]:
            identifier(entry)
    for field, names in {
        'origin': ['task', 'project'], 'context': ['architecture', 'environment'],
        'applicability': ['rationale'], 'correction': ['principle'],
        'verification': ['regression_check', 'attribution'],
        'source': ['revision', 'date'],
    }.items():
        for name in names:
            nonempty(lesson[field][name], f'{field}.{name}')
    dt.date.fromisoformat(lesson['source']['date'])
    facts(lesson['context']['versions'], 'context.versions')
    facts(lesson['applicability']['required_facts'], 'applicability.required_facts')
    required = lesson['applicability']['required_facts']
    if not {'architecture', 'environment'} <= required.keys():
        raise ValueError('applicability needs architecture and environment facts')
    if any(f'version.{component}' not in required for component in lesson['context']['versions']):
        raise ValueError('applicability needs a version fact for each relevant component')
    strings(lesson['exclusions']['counterexamples'], 'exclusions.counterexamples')
    if not isinstance(lesson['exclusions']['any_of'], list):
        raise ValueError('exclusions.any_of must be a list of fact maps')
    for exclusion in lesson['exclusions']['any_of']:
        facts(exclusion, 'exclusion')
    strings(lesson['correction']['project_specific'], 'correction.project_specific', False)
    for field in ['failure_evidence', 'cause_evidence', 'repair_evidence', 'limits']:
        strings(lesson['verification'][field], f'verification.{field}')
    strings(lesson['verification']['additional_evidence'], 'additional_evidence', False)
    if lesson['status'] == 'verified' and not lesson['verification']['additional_evidence']:
        if lesson['applicability']['required_facts'].get('project') != lesson['origin']['project']:
            raise ValueError('one incident must remain scoped to its originating project')
    if lesson['status'] == 'superseded' and not lesson['superseded_by']:
        raise ValueError('superseded records require a replacement reference')


def atomic(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix='.pending-', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
        directory = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def index(root):
    value = json.loads((root / 'INDEX.json').read_text())
    if value.get('schema') != 1 or not isinstance(value.get('lessons'), dict):
        raise ValueError('unsupported or corrupt index')
    return value


def get(root, lesson_id, revision):
    identifier(lesson_id)
    if not re.fullmatch(r'[0-9a-f]{64}', revision):
        raise ValueError('invalid revision')
    value = json.loads((root / 'records' / lesson_id / f'{revision}.json').read_text())
    if digest(value) != revision or value['lesson']['id'] != lesson_id:
        raise ValueError('revision integrity check failed')
    # Expose the exact revision read without changing the immutable record or
    # its digest. A pinned historical read must not report the current head.
    return {**value, 'revision': revision}


def put(root, lesson, expected, reason):
    validate(lesson)
    nonempty(reason, 'reason')
    with (root / '.write.lock').open('a') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise ValueError('busy writer; stop and reread before retrying') from None
        current = index(root)
        lesson_id = lesson['id']
        row = current['lessons'].get(lesson_id)
        previous = row['revision'] if row else None
        existing = get(root, lesson_id, previous) if previous else None
        if expected == 'new' and existing and existing['lesson'] == lesson:
            return {'id': lesson_id, 'revision': previous, 'changed': False}
        if expected != (previous or 'new'):
            raise ValueError('stale revision; reread and reassess, do not overwrite')
        if existing and existing['lesson'] == lesson:
            return {'id': lesson_id, 'revision': previous, 'changed': False}
        snapshot = {
            'lesson': lesson, 'previous_revision': previous, 'reason': reason,
            'recorded_at': dt.datetime.now(dt.UTC).isoformat(),
        }
        revision = digest(snapshot)
        atomic(root / 'records' / lesson_id / f'{revision}.json', encoded(snapshot))
        current['lessons'][lesson_id] = {
            'title': lesson['title'], 'status': lesson['status'], 'failure_kind': lesson['failure_kind'],
            'keywords': lesson['keywords'], 'conditions': lesson['applicability']['required_facts'],
            'conflicts_with': lesson['conflicts_with'],
            'revision': revision,
        }
        atomic(root / 'INDEX.json', encoded(current))
        return {'id': lesson_id, 'revision': revision, 'changed': True}


def applicability(lesson, measured):
    if lesson['status'] != 'verified':
        return 'not-verified'
    required = lesson['applicability']['required_facts']
    exclusions = lesson['exclusions']['any_of']
    if any(key in measured and measured[key] != value for key, value in required.items()):
        return 'inapplicable'
    if any(all(measured.get(k) == v for k, v in group.items()) for group in exclusions):
        return 'inapplicable'
    if any(key not in measured for key in required):
        return 'unknown'
    # An exclusion with no contradicting fact and an unmeasured fact cannot be ruled out.
    if any(not any(k in measured and measured[k] != v for k, v in group.items())
           and any(k not in measured for k in group) for group in exclusions):
        return 'unknown'
    return 'eligible-for-diagnostic-review'


def check(root, current, context, ids):
    if context.get('failure_kind') == 'permission-denial':
        return {lesson_id: 'permission-blocker' for lesson_id in ids}
    if context.get('failure_kind') not in KINDS:
        raise ValueError('context needs a valid failure_kind')
    measured = context['facts']
    facts(measured, 'context facts')
    loaded = {}

    def load(lesson_id):
        if lesson_id not in loaded:
            row = current['lessons'][lesson_id]
            loaded[lesson_id] = get(root, lesson_id, row['revision'])['lesson']
        return loaded[lesson_id]

    result = {}
    for lesson_id in ids:
        lesson = load(lesson_id)
        result[lesson_id] = (applicability(lesson, measured) if lesson['failure_kind'] == context['failure_kind'] else 'inapplicable')
        if result[lesson_id] == 'eligible-for-diagnostic-review':
            # Inspect incoming as well as outgoing declared conflicts, even if only one ID was selected.
            others = set(lesson['conflicts_with'])
            for other_id, other_row in current['lessons'].items():
                if lesson_id in other_row['conflicts_with']:
                    others.add(other_id)
            for other_id in others:
                if other_id not in current['lessons']:
                    result[lesson_id] = 'unresolved-conflict-reference'
                    break
                other = load(other_id)
                if other['status'] == 'verified' and applicability(other, measured) in {'eligible-for-diagnostic-review', 'unknown'}:
                    result[lesson_id] = 'conflict-needs-scope-or-evidence'
                    break
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT, help='Use an isolated root for synthetic tests; not to bypass denied writes.')
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('list', help='Print compact index only')
    p = sub.add_parser('get', help='Read one immutable revision')
    p.add_argument('id'); p.add_argument('--revision')
    p = sub.add_parser('history', help='Print the active revision chain')
    p.add_argument('id')
    p = sub.add_parser('put', help='Save sanitized JSON using lock + expected revision')
    p.add_argument('file', type=Path); p.add_argument('--expected', required=True); p.add_argument('--reason', required=True)
    p = sub.add_parser('check', help='Evaluate measured fact conditions; diagnostic review still required')
    p.add_argument('--context', type=Path, required=True); p.add_argument('ids', nargs='+')
    args = parser.parse_args()
    try:
        if args.command == 'put':
            result = put(args.root, json.loads(args.file.read_text()), args.expected, args.reason)
        else:
            current = index(args.root)
            if args.command == 'list':
                result = current
            elif args.command == 'check':
                result = check(args.root, current, json.loads(args.context.read_text()), args.ids)
            else:
                revision = args.revision if args.command == 'get' and args.revision else current['lessons'][args.id]['revision']
                result = get(args.root, args.id, revision)
                if args.command == 'history':
                    chain = []
                    while revision:
                        value = get(args.root, args.id, revision)
                        chain.append({'revision': revision, 'recorded_at': value['recorded_at'], 'reason': value['reason'], 'status': value['lesson']['status']})
                        revision = value['previous_revision']
                    result = chain
        print(json.dumps(result, indent=2, ensure_ascii=False))
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f'Lesson operation stopped: {error}', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
