import { DeferredBoundary } from "../../src/lib/suite/deferred-boundary";
import { createRoot } from "react-dom/client";
import { lazy, Suspense, useEffect, useRef, useState } from "react";
import { BrowserRouter, Link, Routes, Route, useLocation, guardBrowserHistory } from "../../src/lib/suite/routing";
import { SuiteForm } from "../../src/lib/suite/forms";
import { createStateScope, useFormState } from "../../src/lib/suite/state";
import { fetchResponse, readJson } from "../../src/lib/suite/http";
import { z, validateFields, parseWithSchema } from "../../src/lib/suite/validation";
import { Input } from "../../src/components/ui/input";
import { Button } from "../../src/components/ui/button";
import "./suite-components-context.css";
const scope = createStateScope(() => 0);
const titleSchema = z.object({ title: z.string().trim().min(2, "Enter at least two characters.") });

function SnapshotWriter() {
  const queue = scope.useSnapshot()!;
  const renders = useRef(0); renders.current += 1;
  return <section aria-label="Draft restoration performance">
    <output aria-label="Snapshot writer renders">{renders.current}</output>
    <Button onClick={() => queue.save(n => n + 1)}>Save queue draft</Button>
  </section>;
}

const UnavailablePanel = lazy(async () => { throw new Error("Synthetic panel load failure"); });
function Page() {
  const [loadPanel, setLoadPanel] = useState(false);
  const location = useLocation();
  const [form, setForm] = useFormState({ title: "" });
  const [dirty, setDirty] = useState(false);
  const [busy, setBusy] = useState(false);
  const [notice, setNotice] = useState("");
  const [error, setError] = useState("");
  const shared = scope.useState()!;
  useEffect(() => guardBrowserHistory(() => !dirty || window.confirm("Discard unsaved changes?")), [dirty, location]);
  return <main style={{ padding: 24, maxWidth: 620 }}>
    <h1>Foundation verification</h1>
    <Button onClick={() => setLoadPanel(true)}>Load unavailable panel</Button>
    {loadPanel && <DeferredBoundary><Suspense fallback={<p role="status">Loading panel…</p>}><UnavailablePanel /></Suspense></DeferredBoundary>}<p data-testid="route">{location.hash || "#first"}</p>
    <Link to="#first">First page</Link> <Link to="#second">Second page</Link>
    <SuiteForm aria-label="Example form" aria-busy={busy} onSubmit={async (event) => {
      event.preventDefault(); setError(""); setNotice("");
      const result = validateFields(titleSchema, form);
      if (!result.success) { setError(result.errors.title); return; }
      setBusy(true);
      try {
        await readJson(await fetchResponse("/foundation-save", { method: "POST", body: JSON.stringify(result.data) }), value => parseWithSchema(z.object({ saved: z.literal(true) }), value), { invalidMessage: "Save failed. Retry." });
        setNotice("Saved."); setDirty(false);
      } catch { setError("Save failed. Retry."); }
      finally { setBusy(false); }
    }}>
      <label htmlFor="title">Title</label><Input id="title" required value={form.title} onChange={e => { setForm({ title: e.target.value }); setDirty(true); }} />
      <Button type="submit" disabled={busy}>Save</Button>
      {busy && <p role="status">Saving…</p>}{error && <p role="alert">{error}</p>}{notice && <p role="status">{notice}</p>}
    </SuiteForm>
    <Button onClick={() => setDirty(false)}>Keep draft and clear guard</Button>
    <Button onClick={() => shared.save(n => n + 1)}>Increment shared count</Button><output aria-label="Shared count">{shared.state}</output>
  </main>;
}
function Fixture() {
  const [session, setSession] = useState(0);
  return <BrowserRouter><Button onClick={() => setSession(n => n + 1)}>New session</Button><scope.Provider key={session}><SnapshotWriter /><Routes><Route path="*" element={<Page />} /></Routes></scope.Provider></BrowserRouter>;
}
createRoot(document.getElementById("root")!).render(<Fixture />);
