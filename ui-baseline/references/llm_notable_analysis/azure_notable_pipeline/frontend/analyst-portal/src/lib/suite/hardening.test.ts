// @vitest-environment node
import { afterEach, describe, expect, it, vi } from "vitest";
import { fetchResponse, readJson } from "./http";
import { createLatestRead } from "./query";
afterEach(() => { vi.unstubAllGlobals(); vi.useRealTimers(); });
describe("operation deadlines and read ownership", () => {
  it("preserves no-content responses even when a browser interceptor exposes an empty stream", async () => {
    vi.useFakeTimers(); const response = new Response(null, { status: 204 });
    Object.defineProperty(response, "body", { value: new ReadableStream() });
    vi.stubGlobal("fetch", vi.fn(async () => response));
    expect(await fetchResponse("/logout", { method: "POST" })).toBe(response);
    expect(vi.getTimerCount()).toBe(0);
  });
  it("aborts and cancels a stalled body after headers, preserving timeout classification", async () => {
    vi.useFakeTimers(); const cancel = vi.fn(); let signal: AbortSignal | undefined;
    vi.stubGlobal("fetch", vi.fn(async (_input, init) => { signal = init.signal; return new Response(new ReadableStream({ cancel })); }));
    const response = await fetchResponse("/slow", { timeoutMs: 50 });
    const result = readJson(response, value => value, { invalidMessage: "invalid" }).catch(error => error);
    await vi.advanceTimersByTimeAsync(50);
    expect(await result).toMatchObject({ kind: "timeout", status: 0 });
    expect(signal?.aborted).toBe(true); expect(cancel).toHaveBeenCalledOnce(); expect(vi.getTimerCount()).toBe(0);
  });
  it("caller abort cancels body consumption and releases timer", async () => {
    vi.useFakeTimers(); const cancel = vi.fn(); const caller = new AbortController();
    vi.stubGlobal("fetch", vi.fn(async () => new Response(new ReadableStream({ cancel }))));
    const response = await fetchResponse("/download", { signal: caller.signal, timeoutMs: 120_000 });
    const result = response.blob().catch(error => error); caller.abort();
    expect(await result).toMatchObject({ kind: "cancelled" }); expect(cancel).toHaveBeenCalledOnce(); expect(vi.getTimerCount()).toBe(0);
  });
  it("bounds token preparation and never starts HTTP when the token eventually arrives", async () => {
    vi.useFakeTimers(); let release!: (value: RequestInit) => void;
    const fetcher = vi.fn(); vi.stubGlobal("fetch", fetcher);
    const result = fetchResponse("/protected", { timeoutMs: 50, prepare: () => new Promise(resolve => { release = resolve; }) }).catch(error => error);
    await vi.advanceTimersByTimeAsync(50); expect(await result).toMatchObject({ kind: "timeout" });
    release({ headers: { Authorization: "late-token" } }); await Promise.resolve();
    expect(fetcher).not.toHaveBeenCalled(); expect(vi.getTimerCount()).toBe(0);
  });
  it("honors an explicit long-operation deadline without nesting the default 30 seconds", async () => {
    vi.useFakeTimers(); let finish!: (response: Response) => void; let signal!: AbortSignal;
    vi.stubGlobal("fetch", vi.fn((_input, init) => { signal = init.signal; return new Promise<Response>(resolve => { finish = resolve; }); }));
    const result = fetchResponse("/chat", { timeoutMs: 220_000 });
    await vi.advanceTimersByTimeAsync(31_000); expect(signal.aborted).toBe(false);
    finish(new Response("answer")); expect(await (await result).text()).toBe("answer"); expect(vi.getTimerCount()).toBe(0);
  });
  it("retains metadata, cloning, binary bytes and bodyUsed semantics", async () => {
    vi.stubGlobal("fetch", vi.fn(async () => {
      const response = new Response(new Uint8Array([0, 255, 16]), { headers: { "Content-Disposition": "attachment; filename=test.bin" } });
      Object.defineProperty(response, "url", { value: "https://storage.example.test/file" }); return response;
    }));
    const response = await fetchResponse("/file"); const copy = response.clone();
    expect(response.url).toBe("https://storage.example.test/file"); expect(response.bodyUsed).toBe(false);
    expect([...new Uint8Array(await response.arrayBuffer())]).toEqual([0,255,16]);
    expect(await copy.arrayBuffer()).toHaveProperty("byteLength",3); expect(response.bodyUsed).toBe(true);
  });
  it("does not mislabel a stalled HTTP error body as ordinary validation failure", async () => {
    vi.useFakeTimers(); vi.stubGlobal("fetch", vi.fn(async () => new Response(new ReadableStream(), { status: 503 })));
    const response = await fetchResponse("/error", { timeoutMs: 20 });
    const result = readJson(response, value => value, { invalidMessage: "invalid", readProblem: async r => { try { await r.json(); } catch {} return { detail: "fallback" }; } }).catch(error => error);
    await vi.advanceTimersByTimeAsync(20); expect(await result).toMatchObject({ kind: "timeout" });
  });
  it("supersedes old reads and prevents stale results after a parent cancellation", () => {
    const reads = createLatestRead(); const old = reads.begin(); const caller = new AbortController(); const next = reads.begin(caller.signal);
    expect(old.signal.aborted).toBe(true); expect(old.isCurrent()).toBe(false); expect(next.isCurrent()).toBe(true);
    caller.abort(); expect(next.isCurrent()).toBe(false); next.finish(); reads.cancel();
  });
});
