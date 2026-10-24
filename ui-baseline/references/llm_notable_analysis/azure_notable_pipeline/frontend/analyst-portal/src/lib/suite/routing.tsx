import { BrowserRouter as ReactBrowserRouter, useLocation, type BrowserRouterProps } from "react-router";
export * from "react-router";
const INDEX = "idx";
let installed = false;
let currentHref = "";
let currentState: unknown;
let currentIndex = 0;
let restoring = false;
let programmatic = false;
let evaluatingGuard = false;
let historyGuard: ((next: URL) => boolean) | null = null;
const locationKey = () => window.location.pathname + window.location.search + window.location.hash;
function recordCurrent() {
  currentHref = locationKey(); currentState = window.history.state;
  currentIndex = window.history.state?.[INDEX] ?? currentIndex;
}
function install() {
  if (installed || typeof window === "undefined") return;
  installed = true;
  window.history.replaceState({ ...window.history.state, [INDEX]: window.history.state?.[INDEX] ?? 0 }, "");
  recordCurrent();
  // Install before React Router subscribes so a rejected Back/Forward cannot unmount a dirty editor.
  window.addEventListener("popstate", (event) => {
    if (restoring) { restoring = false; event.stopImmediatePropagation(); recordCurrent(); return; }
    const previous = { index: currentIndex, href: currentHref, state: currentState };
    const nextIndex = window.history.state?.[INDEX];
    let accepted = true;
    evaluatingGuard = true;
    try { accepted = programmatic || !historyGuard || historyGuard(new URL(window.location.href)); }
    finally { evaluatingGuard = false; }
    if (!accepted) {
      event.stopImmediatePropagation();
      const delta = typeof nextIndex === "number" ? previous.index - nextIndex : 0;
      if (delta) { restoring = true; setTimeout(() => window.history.go(delta), 0); }
      else window.history.replaceState(previous.state, "", previous.href);
      return;
    }
    recordCurrent();
  });
  window.addEventListener("hashchange", () => { if (!restoring && !evaluatingGuard) recordCurrent(); });
}
/** All six products use the same React Router browser engine. Routes and permission guards stay app-owned. */
export function BrowserRouter(props: BrowserRouterProps) { install(); return <ReactBrowserRouter {...props} />; }
export function guardBrowserHistory(guard: (next: URL) => boolean): () => void {
  install(); recordCurrent(); historyGuard = guard;
  return () => { if (historyGuard === guard) historyGuard = null; };
}
/** Compatibility for event-driven workspaces; shares React Router's history index and subscription. */
export function navigateBrowser(href: string, options: { replace?: boolean; state?: unknown } = {}, allowed: (next: URL) => boolean = () => true) {
  install(); const next = new URL(href, window.location.href);
  if (next.origin !== window.location.origin || !allowed(next)) return;
  const target = next.pathname + next.search + next.hash;
  const replace = options.replace || target === locationKey();
  const state = options.state === undefined ? window.history.state : options.state;
  const nextState = { ...(state && typeof state === "object" ? state : {}), [INDEX]: currentIndex + (replace ? 0 : 1) };
  window.history[replace ? "replaceState" : "pushState"](nextState, "", target);
  programmatic = true;
  try { window.dispatchEvent(new PopStateEvent("popstate", { state: nextState })); }
  finally { programmatic = false; }
}
export function useBrowserLocation(): string {
  const location = useLocation();
  return location.pathname + location.search + location.hash;
}
