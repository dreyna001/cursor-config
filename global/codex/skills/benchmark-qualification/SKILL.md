---
name: benchmark-qualification
description: "Qualify controlled benchmark runs before comparing or promoting model and system changes."
---

# Benchmark Qualification

Use this skill when a benchmark is being used to select, qualify, or activate a model or system configuration. It is not a general model-training or live-deployment workflow.

## Preserve the comparison

Before drawing conclusions, identify the exact source revision and working-tree changes, built image digest, model/provider/deployment, prompt and policy versions, resource caps, fixture manifest and split, evaluator version, and cost assumptions. Record these with each run. Change the intended comparison factor while keeping the rest fixed; if a run differs in multiple factors, label the result exploratory rather than paired evidence.

Run candidates against the same fixture IDs and evaluator rules. Keep holdout labels and oracle material outside model inputs, retrieval, checkpoints, and ordinary run logs. When external search is needed, use the narrowest fixture-scoped credential available and keep credentials out of prompts and persisted state. Use synthetic adapters for local checks; live qualification requires the user's authorization for that environment and data.

When semantic parity is a decision criterion, compare the actual input contracts and paired fixtures. If automated scoring cannot resolve parity, disclose the confounder and use independent review proportional to the decision; a model peer is allowed but must be labeled as model review. Do not make human review a new blocker for already authorized synthetic work. Keep any required human acceptance separate from model review.

Preserve every attempt under a distinct run identity. Mark failed, interrupted, and incomplete runs explicitly; do not overwrite them with a successful rerun or silently omit them from the comparison. A rerun may repair evidence, but it does not erase the earlier outcome.

## Judge evidence at the right level

Keep semantic quality, actual work performed, resource use, and operational completion as distinct measures. Report raw observations and evaluator limitations alongside aggregates. A model grader is a secondary signal; it does not establish human acceptance. Claim human acceptance only when a human supplied that judgment.

Honor the project's documented training and holdout minimums for cost fitting; do not carry a numeric minimum from one project into another. If the required holdout evidence is missing or the exact configuration does not match the run, label the estimate or fit as unqualified rather than activating it.

Recommend activation only when the predeclared quality criteria and work evidence support it on the exact source, image, model, caps, and fixtures being considered. A model-judge score, cost estimate, or successful single run alone is insufficient. This skill does not authorize deployment or activation; follow the user's permissions for those actions.

## Report the result

State which artifact/configuration was measured, which attempts failed or were skipped, whether the comparison was paired, and what the evidence supports. Separate observed results from inference and remaining uncertainty. Do not infer performance from function length, scanner similarity, or other proxy metrics when the benchmark does not measure that property.
