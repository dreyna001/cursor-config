/** A lifecycle-owned latest read. No caching, implicit retries, or mutation replay. */
export function createLatestRead() {
  let current: AbortController | null = null;
  return {
    begin(parent?: AbortSignal) {
      current?.abort();
      const controller = new AbortController();
      current = controller;
      const cancel = () => controller.abort();
      if (parent?.aborted) cancel();
      else parent?.addEventListener("abort", cancel, { once: true });
      return {
        signal: controller.signal,
        isCurrent: () => current === controller && !controller.signal.aborted,
        finish: () => { parent?.removeEventListener("abort", cancel); },
        cancel: () => { cancel(); parent?.removeEventListener("abort", cancel); },
      };
    },
    cancel() { current?.abort(); current = null; },
  };
}
