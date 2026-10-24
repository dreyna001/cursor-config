import { ChevronUp, LogOut, UserRound } from "lucide-react";
import { useEffect, useId, useRef, useState } from "react";
import { createPortal } from "react-dom";

type WorkspaceAccountProps = {
  name?: string;
  accountId?: string;
  onSignOut: () => void;
};

/** Shared presentation only; each app retains its identity and sign-out handler. */
export function WorkspaceAccount({ name, accountId, onSignOut }: WorkspaceAccountProps) {
  const label = name?.trim() || accountId?.trim() || "Signed in";
  const words = (name?.trim() || accountId?.trim() || "").split("@")[0].split(/[\s._-]+/).filter(Boolean);
  const initials = words.length ? [words[0][0], ...(words.length > 1 ? [words[words.length - 1][0]] : [])].join("").toLocaleUpperCase() : "";
  const id = useId();
  const trigger = useRef<HTMLButtonElement>(null);
  const panel = useRef<HTMLDivElement>(null);
  const [position, setPosition] = useState<{ left: number; bottom: number; width: number; maxHeight: number } | null>(null);

  useEffect(() => {
    if (!position) return;
    panel.current?.querySelector("button")?.focus();
    const closeOutside = (event: Event) => {
      if (event.target instanceof Node && !trigger.current?.contains(event.target) && !panel.current?.contains(event.target)) setPosition(null);
    };
    const escape = (event: KeyboardEvent) => {
      if (event.key !== "Escape") return;
      event.preventDefault();
      setPosition(null);
      trigger.current?.focus();
    };
    const close = () => setPosition(null);
    document.addEventListener("pointerdown", closeOutside);
    document.addEventListener("focusin", closeOutside);
    document.addEventListener("keydown", escape);
    window.addEventListener("resize", close);
    return () => {
      document.removeEventListener("pointerdown", closeOutside);
      document.removeEventListener("focusin", closeOutside);
      document.removeEventListener("keydown", escape);
      window.removeEventListener("resize", close);
    };
  }, [position]);

  return <div className="workspace-account">
    <button ref={trigger} className="workspace-account-trigger" type="button" aria-label={`Account: ${label}`}
      aria-expanded={position !== null} aria-controls={position ? id : undefined} title={label}
      onClick={() => {
        const row = trigger.current!.getBoundingClientRect();
        setPosition(position ? null : { left: row.left, bottom: window.innerHeight - row.top + 8, width: row.width, maxHeight: Math.max(0, row.top - 24) });
      }}>
      <span className="workspace-account-avatar" aria-hidden="true">{initials || <UserRound size={16} />}</span>
      <span className="workspace-account-label"><span className="workspace-account-name">{label}</span><span className="workspace-account-caption">Account</span></span>
      <ChevronUp className="workspace-account-chevron" size={16} aria-hidden="true" />
    </button>
    {position && createPortal(<div ref={panel} id={id} className="workspace-account-panel workspace-typography" role="region" aria-label="Account details" style={position}
      onKeyDown={event => {
        if (event.key === "Tab") {
          setPosition(null);
          // Continue the browser's normal tab order from the sidebar trigger.
          trigger.current?.focus();
        }
      }}
      onBlur={event => {
        if (!event.currentTarget.contains(event.relatedTarget) && !trigger.current?.contains(event.relatedTarget)) setPosition(null);
      }}>
      <div className="workspace-account-details"><p className="workspace-account-name">{label}</p>{accountId && accountId !== label ? <p className="workspace-account-id">{accountId}</p> : null}</div>
      <button type="button" className="workspace-account-signout" onClick={() => { setPosition(null); trigger.current?.focus(); onSignOut(); }}><LogOut size={16} aria-hidden="true" />Sign out</button>
    </div>, document.body)}
  </div>;
}
