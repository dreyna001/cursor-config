import { Component, type ReactNode } from "react";
import { Button } from "../../components/ui/button";
/** Keep the owning shell and unsaved-work guards mounted if a deferred panel cannot load. */
export class DeferredBoundary extends Component<{ children: ReactNode; active?: boolean }, { failed: boolean; visited: boolean }> {
  state = { failed: false, visited: this.props.active !== false };
  static getDerivedStateFromProps(props: { active?: boolean }, state: { visited: boolean }) {
    return props.active !== false && !state.visited ? { visited: true } : null;
  }
  static getDerivedStateFromError() { return { failed: true }; }
  render() {
    // Delay the first mount only. Afterwards retain the panel's drafts and focus state.
    if (!this.state.visited) return null;
    if (this.state.failed) return <section role="alert">
      <p>This part of the workspace could not load. Reload the workspace to try again.</p>
      <Button type="button" onClick={() => window.location.reload()}>Reload workspace</Button>
    </section>;
    return this.props.children;
  }
}
