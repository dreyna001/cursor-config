import * as React from "react";
import * as DialogPrimitive from "@radix-ui/react-dialog";
import { X } from "lucide-react";
import { Button } from "./button";
import { cn } from "../../lib/utils";
import "./suite-components.css";

export type DialogProps = {
  open: boolean;
  title: string;
  description?: React.ReactNode;
  children?: React.ReactNode;
  actions?: React.ReactNode;
  onClose: () => void;
  busy?: boolean;
  role?: "dialog" | "alertdialog";
  size?: "default" | "wide";
  showClose?: boolean;
  dismissOnOutside?: boolean;
  initialFocusRef?: React.RefObject<HTMLButtonElement | null>;
  className?: string;
};

export function Dialog({ open, title, description, children, actions, onClose, busy = false, role = "dialog", size = "default", showClose = true, dismissOnOutside = false, initialFocusRef, className }: DialogProps) {
  const opener = React.useRef<HTMLElement | null>(null);
  const content = React.useRef<HTMLDivElement>(null);
  React.useEffect(() => {
    // Native focus can leave a button when it becomes disabled during a request.
    // Keep a focusable modal target even when every action is temporarily disabled.
    if (open && busy) content.current?.focus({ preventScroll: true });
  }, [open, busy]);
  return <DialogPrimitive.Root open={open} onOpenChange={next => { if (!next && !busy) onClose(); }}>
    <DialogPrimitive.Portal>
      <DialogPrimitive.Overlay className="suite-dialog-overlay workspace-motion-overlay" onClick={() => { if (dismissOnOutside && !busy) onClose(); }} />
      <DialogPrimitive.Content ref={content} role={role} aria-modal="true" {...(!description ? { "aria-describedby": undefined } : {})}
        className={cn("suite-dialog workspace-typography workspace-popup-viewport", size === "wide" && "suite-dialog--wide", className)}
        data-suite-component="dialog" data-size={size} aria-busy={busy || undefined}
        onOpenAutoFocus={event => {
          opener.current = document.activeElement instanceof HTMLElement ? document.activeElement : null;
          if (initialFocusRef?.current) {
            event.preventDefault();
            if (!initialFocusRef.current.disabled) initialFocusRef.current.focus();
            else content.current?.focus();
          }
        }}
        onCloseAutoFocus={event => { event.preventDefault(); if (opener.current?.isConnected) opener.current.focus({ preventScroll: true }); }}
        onEscapeKeyDown={event => { if (busy) event.preventDefault(); }}
        onKeyDown={event => { if (busy && event.key === "Tab") { event.preventDefault(); content.current?.focus({ preventScroll: true }); } }}
        onInteractOutside={event => { event.preventDefault(); }}>
        <header className="suite-dialog-header">
          <DialogPrimitive.Title className="suite-dialog-title">{title}</DialogPrimitive.Title>
          {showClose && <DialogPrimitive.Close asChild><Button variant="ghost" size="icon" aria-label="Close" disabled={busy}><X size={18} aria-hidden="true" /></Button></DialogPrimitive.Close>}
        </header>
        <div className="suite-dialog-body">
          {description && <DialogPrimitive.Description className="suite-dialog-description">{description}</DialogPrimitive.Description>}
          {children}
        </div>
        {actions && <footer className="suite-dialog-actions workspace-dialog-actions">{actions}</footer>}
      </DialogPrimitive.Content>
    </DialogPrimitive.Portal>
  </DialogPrimitive.Root>;
}
