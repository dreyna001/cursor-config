# Security and Evidence Discipline

- **Do not fabricate** IOCs, events, IDs, or findings. Mark unsupported factual claims as `unknown` or omit per contract.
- **Evidence vs inference:** label or separate analyst conclusions from raw source material; do not present inference as ground truth.
- Preserve raw evidence or diagnostic metadata when humans must review failures.
- Fail closed for policy or action paths. Non-consequential analysis may degrade only with an explicit, observable reason.
- Preserve independent supported observations and the intended analytical decision
  when correcting another unsupported field; unsupported output shape is not proof
  that the underlying event is benign or absent.
- Distinguish observed zero results and scoped missing records from an unqueried,
  unavailable or failed source. Retain source/query provenance and coverage limits.
- A stricter check needs supported controls that detect lost facts or decisions as
  well as unsupported controls that detect false acceptance. Preserve failures for
  review instead of relaxing checks or relabeling cases to manufacture success.
