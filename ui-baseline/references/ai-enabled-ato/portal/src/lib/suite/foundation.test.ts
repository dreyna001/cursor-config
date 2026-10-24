// @vitest-environment node
import { afterEach, describe, expect, it, vi } from "vitest";
import { ApiError, fetchResponse, readJson, requestScope } from "./http";
import { parseWithSchema, validateFields, z } from "./validation";
afterEach(() => { vi.unstubAllGlobals(); vi.useRealTimers(); });
describe("suite request and validation boundaries", () => {
  it("preserves credentials and headers and never retries a rejected write", async () => {
    const fetcher = vi.fn().mockRejectedValue(new TypeError("offline")); vi.stubGlobal("fetch", fetcher);
    await expect(fetchResponse("/write", { method: "POST", credentials: "include", headers: { "X-CSRF-Token": "test" }, body: "draft" })).rejects.toThrow("offline");
    expect(fetcher).toHaveBeenCalledTimes(1);
    expect(fetcher.mock.calls[0][1]).toMatchObject({ method: "POST", credentials: "include", body: "draft", headers: { "X-CSRF-Token": "test" } });
  });
  it("does not send a pre-cancelled request", async () => {
    const fetcher = vi.fn(); vi.stubGlobal("fetch", fetcher); const controller = new AbortController(); controller.abort();
    await expect(fetchResponse("/read", { signal: controller.signal })).rejects.toMatchObject({ kind: "cancelled", status: 0 });
    expect(fetcher).not.toHaveBeenCalled();
  });
  it("distinguishes a deadline from caller cancellation and clears timers", async () => {
    vi.useFakeTimers(); const scope = requestScope(50); await vi.advanceTimersByTimeAsync(50);
    expect(scope.signal.aborted).toBe(true); expect(() => scope.classify(new Error())).toThrow("Request timed out."); scope.cleanup();
    const controller = new AbortController(); const other = requestScope(50, controller.signal); controller.abort();
    try { other.classify(new Error()); } catch (error) { expect(error).toMatchObject({ kind: "cancelled" }); }
    other.cleanup(); expect(vi.getTimerCount()).toBe(0);
  });
  it("releases cancellation listeners and deadlines after a successful request", async () => {
    vi.useFakeTimers(); const response = new Response("ok"); vi.stubGlobal("fetch", vi.fn().mockResolvedValue(response));
    const received = await fetchResponse("/read"); expect(await received.text()).toBe("ok"); expect(vi.getTimerCount()).toBe(0);
  });
  it("preserves adapter-owned upload/stream deadlines without adding a timeout", async () => {
    vi.useFakeTimers(); const fetcher = vi.fn().mockResolvedValue(new Response("ok")); vi.stubGlobal("fetch", fetcher);
    await fetchResponse("https://storage.invalid/signed", { method: "POST", timeoutMs: 0, body: "file" });
    expect(fetcher).toHaveBeenCalledWith("https://storage.invalid/signed", { method: "POST", body: "file" }); expect(vi.getTimerCount()).toBe(0);
  });
  it("retains structured HTTP errors and rejects invalid successful responses", async () => {
    const options = { invalidMessage: "Invalid response", readProblem: async () => ({ detail: "Review the field", errorCode: "invalid", fieldErrors: [{ path: "title", code: "required", message: "Required" }] }) };
    await expect(readJson(new Response("{}", { status: 422 }), () => null, options)).rejects.toMatchObject({ status: 422, errorCode: "invalid", fieldErrors: [{ path: "title" }] });
    for (const body of ["not json", "{}"])
      await expect(readJson(new Response(body), () => null, options)).rejects.toMatchObject({ status: 502, kind: "invalid_response" });
  });
  it("preserves schema transforms/defaults and returns keyed validation issues", () => {
    const schema = z.object({ title: z.string().trim().min(1, "Required"), count: z.number().default(1) });
    expect(parseWithSchema(schema, { title: "  Title " })).toEqual({ title: "Title", count: 1 });
    expect(parseWithSchema(schema, { title: 4 })).toBeNull();
    expect(validateFields(schema, { title: " " })).toMatchObject({ success: false, errors: { title: "Required" } });
    expect(new ApiError(409, "Stale version")).toMatchObject({ status: 409, kind: "http", name: "ApiError" });
  });
});
