# Local Embedding Runtime Practices

Use this for local `sentence-transformers` or Hugging Face Transformers embedding and reranking paths. Preserve the project's approved model-origin and deployment requirements.

- Treat model artifacts and their loader code as supply-chain inputs. Record the model ID and immutable repository commit, license/provenance, artifact digests, and the exact `sentence-transformers`, `transformers`, framework, and tokenizer dependencies. Stage approved artifacts into a controlled cache or image for production and air-gapped deployment; do not make runtime behavior depend on a mutable branch or whatever happens to be cached.
- Keep `trust_remote_code` disabled by default. Enable it only when the selected model requires repository code and that exact code revision has been reviewed and approved; pin the code revision as well as the weight revision. Prefer `safetensors` weights when available and compatible, and verify any converted artifact before deployment.
- Treat model ID/revision, tokenizer, Sentence Transformers module and pooling configuration, query/document prompt, input truncation, output dimension/precision/normalization, and similarity metric as one embedding contract. Use `encode_query()` and `encode_document()` where the model defines distinct retrieval prompts. Changing any contract field requires evaluation and a coordinated index rebuild or migration; do not silently mix vectors from incompatible revisions.
- Qualify the actual inference backend, device, dtype, library versions, and target hardware together. Test startup, memory use, batching, maximum input length, concurrency, and fallback behavior on the deployment path. CPU, accelerator, and alternate inference backends can differ in availability and numerical behavior; select batch and precision settings from measured latency, memory, and retrieval quality rather than a universal default.
- Evaluate candidate changes on representative, held-out queries and corpus data using relevance judgments, including filters, empty results, and tenant boundaries. Compare retrieval quality and operational latency/memory against the current contract. Model-card or public benchmark scores help shortlist candidates; they do not establish fit for the production corpus. Log model revision and execution metadata without logging sensitive input text.

## Sources

- [Sentence Transformers model loading parameters](https://www.sbert.net/docs/package_reference/sentence_transformer/model.html)
- [Sentence Transformers retrieval usage](https://sbert.net/docs/sentence_transformer/usage/usage.html)
- [Sentence Transformers embedding evaluation](https://www.sbert.net/docs/sentence_transformer/usage/mteb_evaluation.html)
- [Transformers model loading and custom-code security](https://huggingface.co/docs/transformers/main/models)
- [Safetensors weight conversion guidance](https://huggingface.co/docs/safetensors/en/convert-weights)
