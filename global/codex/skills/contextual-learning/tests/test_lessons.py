"""SYNTHETIC TEST FIXTURES ONLY: never retained as real learned facts."""
import copy
import fcntl
import importlib.util
import json
import multiprocessing
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'lessons.py'
spec = importlib.util.spec_from_file_location('lesson_store', SCRIPT)
store = importlib.util.module_from_spec(spec)
spec.loader.exec_module(store)
TEMPLATE = json.loads(Path(os.environ.get('CONTEXTUAL_LEARNING_TEMPLATE', str(Path(__file__).resolve().parents[1] / 'references' / 'lesson-template.json'))).read_text())


def fixture(lesson_id='synthetic-atomic-file'):
    lesson = copy.deepcopy(TEMPLATE)
    lesson.update(id=lesson_id, title='SYNTHETIC: complete file publication', status='verified',
                  problem='SYNTHETIC reader saw a partial file after truncate-and-write.',
                  causal_principle='SYNTHETIC single-filesystem rename publishes a complete file.',
                  keywords=['synthetic', 'file', 'atomic'])
    lesson['origin'] = {'task': 'SYNTHETIC test only', 'project': 'synthetic-local-files'}
    lesson['context'] = {'architecture': 'single local filesystem', 'environment': 'Linux local test', 'versions': {'python': '3.12'}}
    lesson['applicability'] = {'required_facts': {'project': 'synthetic-local-files', 'architecture': 'single local filesystem', 'environment': 'Linux local test', 'version.python': '3.12'}, 'rationale': 'SYNTHETIC single incident; keep project scope'}
    lesson['exclusions'] = {'any_of': [{'storage': 'network'}], 'counterexamples': ['SYNTHETIC network-backed or cross-filesystem storage requires different evidence.']}
    lesson['verification'] = {'failure_evidence': ['SYNTHETIC truncated file observed'], 'cause_evidence': ['SYNTHETIC writer opened with truncate before publishing'], 'repair_evidence': ['SYNTHETIC rename presents complete content'], 'regression_check': 'SYNTHETIC deterministic test only', 'limits': ['Not a real incident'], 'additional_evidence': [], 'attribution': 'Synthetic test author'}
    lesson['source'] = {'revision': 'synthetic-fixture-v1', 'date': '2026-10-12'}
    lesson['status_reason'] = 'SYNTHETIC verified marker for testing only'
    return lesson


def measured(**changes):
    facts = dict(fixture()['applicability']['required_facts'], storage='local')
    facts.update(changes)
    return {'failure_kind': 'application-bug', 'facts': facts}


def competing_writer(root, barrier, queue, title):
    lesson = fixture('synthetic-race')
    lesson['title'] = title
    barrier.wait(timeout=5)
    try:
        store.put(Path(root), lesson, 'new', 'SYNTHETIC concurrent writer')
        queue.put('saved')
    except ValueError:
        queue.put('conflict')


class Lessons(unittest.TestCase):

    def test_default_root_honors_custom_codex_home(self):
        with tempfile.TemporaryDirectory(prefix='synthetic-codex-home-') as directory:
            with patch.dict(os.environ, {'CODEX_HOME': directory}):
                configured_spec = importlib.util.spec_from_file_location('configured_lesson_store', SCRIPT)
                configured = importlib.util.module_from_spec(configured_spec)
                configured_spec.loader.exec_module(configured)
                self.assertEqual(configured.ROOT, Path(directory) / 'learning')
                self.assertFalse(configured.ROOT.exists())

    def test_empty_codex_home_uses_current_home(self):
        with patch.dict(os.environ, {'CODEX_HOME': ''}):
            configured_spec = importlib.util.spec_from_file_location('default_lesson_store', SCRIPT)
            configured = importlib.util.module_from_spec(configured_spec)
            configured_spec.loader.exec_module(configured)
            self.assertEqual(configured.ROOT, Path.home() / '.codex' / 'learning')
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='synthetic-contextual-learning-')
        self.root = Path(self.temp.name)
        (self.root / 'INDEX.json').write_bytes(store.encoded({'schema': 1, 'lessons': {}}))
        self.lesson = fixture()
        self.saved = store.put(self.root, self.lesson, 'new', 'SYNTHETIC fixture')

    def tearDown(self):
        self.temp.cleanup()

    def check(self, context, *ids):
        return store.check(self.root, store.index(self.root), context, list(ids or [self.lesson['id']]))

    def test_applicable_lesson_requires_diagnostic_review(self):
        self.assertEqual(set(self.check(measured()).values()), {'eligible-for-diagnostic-review'})

    def test_get_exposes_read_revision_without_rewriting_record(self):
        revision = self.saved['revision']
        path = self.root / 'records' / self.lesson['id'] / f'{revision}.json'
        before = path.read_bytes()
        read = store.get(self.root, self.lesson['id'], revision)
        self.assertEqual(read['revision'], revision)
        self.assertEqual(path.read_bytes(), before)
        self.assertNotIn('revision', json.loads(before))

    def test_pinned_historical_read_returns_its_revision_and_rejects_stale_write(self):
        previous = self.saved['revision']
        updated = copy.deepcopy(self.lesson)
        updated['title'] = 'SYNTHETIC revised evidence'
        current = store.put(self.root, updated, previous, 'SYNTHETIC refinement')['revision']
        historical = store.get(self.root, self.lesson['id'], previous)
        self.assertEqual(historical['revision'], previous)
        self.assertEqual(store.get(self.root, self.lesson['id'], current)['revision'], current)
        with self.assertRaisesRegex(ValueError, 'stale revision'):
            store.put(self.root, self.lesson, historical['revision'], 'SYNTHETIC stale read')

    def test_cli_get_revision_can_be_used_for_unchanged_update(self):
        import subprocess
        import sys
        read = json.loads(subprocess.check_output([
            sys.executable, str(SCRIPT), '--root', str(self.root), 'get', self.lesson['id'],
        ], text=True))
        result = store.put(self.root, read['lesson'], read['revision'], 'SYNTHETIC no-op')
        self.assertFalse(result['changed'])

    def test_same_symptom_in_different_architecture_is_rejected(self):
        self.assertEqual(set(self.check(measured(architecture='distributed object store')).values()), {'inapplicable'})

    def test_unknown_version_or_exclusion_stays_unknown(self):
        for key in ['version.python', 'storage']:
            context = measured()
            del context['facts'][key]
            self.assertEqual(set(self.check(context).values()), {'unknown'})

    def test_excluded_environment_is_rejected(self):
        self.assertEqual(set(self.check(measured(storage='network')).values()), {'inapplicable'})

    def test_conflict_blocks_reuse_and_superseding_resolves_it(self):
        other = fixture('synthetic-conflict')
        other['conflicts_with'] = [self.lesson['id']]
        revision = store.put(self.root, other, 'new', 'SYNTHETIC conflicting guidance')['revision']
        self.assertEqual(set(self.check(measured()).values()), {'conflict-needs-scope-or-evidence'})
        other['status'] = 'superseded'
        other['superseded_by'] = [self.lesson['id']]
        store.put(self.root, other, revision, 'SYNTHETIC evidence resolution')
        self.assertEqual(set(self.check(measured()).values()), {'eligible-for-diagnostic-review'})

    def test_permission_blocker_never_becomes_technical_repair(self):
        context = measured()
        context['failure_kind'] = 'permission-denial'
        self.assertEqual(set(self.check(context).values()), {'permission-blocker'})

    def test_candidates_and_attributed_feedback_do_not_act_as_proof(self):
        for status in ['candidate', 'attributed-feedback']:
            lesson = fixture('synthetic-' + status)
            lesson['status'] = status
            store.put(self.root, lesson, 'new', 'SYNTHETIC uncertain feedback')
            self.assertEqual(set(self.check(measured(), lesson['id']).values()), {'not-verified'})

    def test_one_incident_cannot_drop_its_project_condition(self):
        lesson = fixture('synthetic-overbroad')
        del lesson['applicability']['required_facts']['project']
        with self.assertRaisesRegex(ValueError, 'originating project'):
            store.put(self.root, lesson, 'new', 'SYNTHETIC overgeneralization')

    def test_idempotent_replay_and_stale_update(self):
        before = (self.root / 'INDEX.json').read_bytes()
        self.assertFalse(store.put(self.root, self.lesson, 'new', 'SYNTHETIC replay')['changed'])
        self.assertEqual((self.root / 'INDEX.json').read_bytes(), before)
        revised = copy.deepcopy(self.lesson)
        revised['title'] = 'SYNTHETIC corrected scope'
        current = store.put(self.root, revised, self.saved['revision'], 'SYNTHETIC refine')['revision']
        with self.assertRaisesRegex(ValueError, 'stale revision'):
            store.put(self.root, self.lesson, self.saved['revision'], 'SYNTHETIC stale writer')
        # Rollback is a new revision, preserving both the previous revision and unrelated records.
        other = fixture('synthetic-unrelated')
        store.put(self.root, other, 'new', 'SYNTHETIC unrelated')
        rollback = store.put(self.root, self.lesson, current, 'SYNTHETIC rollback')['revision']
        self.assertEqual(store.get(self.root, self.lesson['id'], rollback)['previous_revision'], current)
        self.assertEqual(store.get(self.root, self.lesson['id'], self.saved['revision'])['lesson'], self.lesson)
        self.assertIn(other['id'], store.index(self.root)['lessons'])

    def test_held_lock_fails_without_retry_or_overwrite(self):
        before = (self.root / 'INDEX.json').read_bytes()
        with (self.root / '.write.lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            with self.assertRaisesRegex(ValueError, 'busy writer'):
                store.put(self.root, fixture('synthetic-locked'), 'new', 'SYNTHETIC lock contention')
        self.assertEqual((self.root / 'INDEX.json').read_bytes(), before)

    def test_actual_permission_error_preserves_index(self):
        before = (self.root / 'INDEX.json').read_bytes()
        (self.root / '.write.lock').chmod(0o400)
        try:
            with self.assertRaises(PermissionError):
                store.put(self.root, fixture('synthetic-denied'), 'new', 'SYNTHETIC denied write')
        finally:
            (self.root / '.write.lock').chmod(0o600)
        self.assertEqual((self.root / 'INDEX.json').read_bytes(), before)

    def test_interruption_before_index_commit_leaves_previous_lesson_active(self):
        before = (self.root / 'INDEX.json').read_bytes()
        original_atomic = store.atomic
        def interrupt(path, content):
            if path.name == 'INDEX.json':
                raise OSError('SYNTHETIC interrupted commit')
            original_atomic(path, content)
        with patch.object(store, 'atomic', side_effect=interrupt):
            with self.assertRaises(OSError):
                store.put(self.root, fixture('synthetic-interrupted'), 'new', 'SYNTHETIC interruption')
        self.assertEqual((self.root / 'INDEX.json').read_bytes(), before)
        self.assertNotIn('synthetic-interrupted', store.index(self.root)['lessons'])

    def test_two_processes_cannot_overwrite_each_other(self):
        ctx = multiprocessing.get_context('fork')
        barrier = ctx.Barrier(2)
        queue = ctx.Queue()
        processes = [ctx.Process(target=competing_writer, args=(str(self.root), barrier, queue, f'SYNTHETIC writer {i}')) for i in range(2)]
        for process in processes:
            process.start()
        for process in processes:
            process.join(timeout=8)
            self.assertEqual(process.exitcode, 0)
        self.assertCountEqual([queue.get(timeout=2), queue.get(timeout=2)], ['saved', 'conflict'])
        row = store.index(self.root)['lessons']['synthetic-race']
        self.assertIn(store.get(self.root, 'synthetic-race', row['revision'])['lesson']['title'], ['SYNTHETIC writer 0', 'SYNTHETIC writer 1'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
