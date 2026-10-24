/** Shared transport. App adapters retain identity, CSRF, schemas and mutation reconciliation. */
export type ApiErrorKind = "cancelled" | "timeout" | "http" | "invalid_response";
export type ProblemFieldError = { path: string; code: string; message: string };
export class ApiError extends Error {
  constructor(public status: number, message: string, public kind: ApiErrorKind = "http",
    public errorCode?: string, public fieldErrors?: ProblemFieldError[]) {
    super(message); this.name = "ApiError";
  }
}
export function isCancelledRequest(error: unknown, signal?: AbortSignal): boolean {
  return Boolean(signal?.aborted) || error instanceof ApiError && error.kind === "cancelled";
}
export type RequestOptions = RequestInit & {
  timeoutMs?: number;
  /** Preparation consumes the same deadline; a late token must never start a request. */
  prepare?: (signal: AbortSignal) => Promise<RequestInit>;
};
/** Zero is reserved for streams whose adapter owns an explicit idle/cancellation policy. No retries. */
export function requestScope(timeoutMs: number, callerSignal?: AbortSignal | null) {
  const controller = new AbortController();
  let timedOut = false;
  const failure = () => new ApiError(0, timedOut ? "Request timed out." : "Request cancelled.", timedOut ? "timeout" : "cancelled");
  const cancel = () => controller.abort(callerSignal?.reason);
  if (callerSignal?.aborted) cancel();
  else callerSignal?.addEventListener("abort", cancel, { once: true });
  const timer = timeoutMs > 0 ? setTimeout(() => { if (!controller.signal.aborted) { timedOut = true; controller.abort(); } }, timeoutMs) : undefined;
  function throwIfAborted() { if (controller.signal.aborted) throw failure(); }
  return {
    signal: controller.signal,
    throwIfAborted,
    classify(error: unknown): never { throwIfAborted(); throw error; },
    async run<T>(operation: () => Promise<T>): Promise<T> {
      throwIfAborted();
      let abort: () => void = () => undefined;
      const aborted = new Promise<never>((_, reject) => {
        abort = () => reject(failure());
        controller.signal.addEventListener("abort", abort, { once: true });
      });
      try {
        const result = await Promise.race([operation(), aborted]);
        throwIfAborted();
        return result;
      } finally { controller.signal.removeEventListener("abort", abort); }
    },
    cleanup() { clearTimeout(timer); callerSignal?.removeEventListener("abort", cancel); },
  };
}
const responseChecks = new WeakMap<Response, () => void>();
export async function fetchResponse(input: RequestInfo | URL, { timeoutMs = 30_000, signal, prepare, ...init }: RequestOptions = {}): Promise<Response> {
  if (timeoutMs === 0 && !prepare) {
    if (signal?.aborted || input instanceof Request && input.signal.aborted) throw new ApiError(0, "Request cancelled.", "cancelled");
    return fetch(input, { ...init, ...(signal ? { signal } : {}) });
  }
  const scope = requestScope(timeoutMs, signal ?? (input instanceof Request ? input.signal : undefined));
  try {
    const prepared = prepare ? await scope.run(() => prepare(scope.signal)) : {};
    scope.throwIfAborted();
    const response = await scope.run(() => fetch(input, { ...init, ...prepared,
      ...(timeoutMs > 0 || signal || input instanceof Request ? { signal: scope.signal } : {}),
    }));
    if ([101, 204, 205, 304].includes(response.status) || !response.body || timeoutMs === 0 && !signal && !(input instanceof Request)) { scope.cleanup(); return response; }
    const reader = response.body.getReader();
    let finished = false;
    let abort: () => void = () => undefined;
    const finish = () => {
      if (finished) return;
      finished = true;
      scope.signal.removeEventListener("abort", abort);
      scope.cleanup();
    };
    const body = new ReadableStream<Uint8Array>({
      start(controller) {
        abort = () => {
          if (finished) return;
          try { scope.throwIfAborted(); } catch (error) { controller.error(error); }
          finish();
          void reader.cancel().catch(() => undefined);
        };
        scope.signal.addEventListener("abort", abort, { once: true });
        if (scope.signal.aborted) abort();
      },
      async pull(controller) {
        try {
          const chunk = await scope.run(() => reader.read());
          if (finished) return;
          if (chunk.done) { finish(); controller.close(); }
          else controller.enqueue(chunk.value);
        } catch (error) {
          if (!finished) { finish(); controller.error(error); void reader.cancel().catch(() => undefined); }
        }
      },
      async cancel(reason) { finish(); await reader.cancel(reason); },
    });
    const wrapped = new Response(body, { status: response.status, statusText: response.statusText, headers: response.headers });
    // Preserve fetch metadata (including signed-download redirects); clone() still tees the guarded body.
    for (const key of ["url", "redirected", "type"] as const) Object.defineProperty(wrapped, key, { value: response[key] });
    function guardReaders(response: Response): Response {
      responseChecks.set(response, scope.throwIfAborted);
      // Native body readers can translate a stream's abort reason into a TypeError.
      // Keep the operation's actual timeout/cancellation cause at the API boundary.
      for (const method of ["arrayBuffer", "blob", "formData", "json", "text"] as const) {
        const read = response[method].bind(response);
        Object.defineProperty(response, method, { value: async () => {
          try { return await read(); } catch (error) { return scope.classify(error); }
        } });
      }
      const clone = response.clone.bind(response);
      Object.defineProperty(response, "clone", { value: () => {
        const copy = clone();
        for (const key of ["url", "redirected", "type"] as const) Object.defineProperty(copy, key, { value: response[key] });
        return guardReaders(copy);
      } });
      return response;
    }
    return guardReaders(wrapped);
  } catch (error) { scope.cleanup(); return scope.classify(error); }
}
export type ResponseParser<T> = (value: unknown) => T | null;
export type Problem = { detail: string; errorCode?: string; fieldErrors?: ProblemFieldError[] };
export async function readJson<T>(response: Response, parse: ResponseParser<T>, options: {
  invalidMessage: string;
  readProblem?: (response: Response) => Promise<Problem>;
}): Promise<T> {
  if (!response.ok) {
    const problem = options.readProblem ? await options.readProblem(response) : { detail: response.statusText };
    responseChecks.get(response)?.();
    throw new ApiError(response.status, problem.detail, "http", problem.errorCode, problem.fieldErrors);
  }
  let value: unknown;
  try { value = await response.json(); }
  catch (error) { if (error instanceof ApiError) throw error; throw new ApiError(502, options.invalidMessage, "invalid_response"); }
  const result = parse(value);
  if (result === null) throw new ApiError(502, options.invalidMessage, "invalid_response");
  return result;
}
