import { useRef, type ReactNode } from "react";
import { Button } from "./button";
import { Dialog } from "./dialog";

export type ConfirmDialogProps = {
  open: boolean; title: string; description: string; error?: string | null;
  confirmLabel?: string; cancelLabel?: string; confirming?: boolean; confirmingLabel?: string;
  additionalAction?: ReactNode; onConfirm: () => void; onCancel: () => void;
};

export function ConfirmDialog({ open, title, description, error, confirmLabel = "Confirm", cancelLabel = "Cancel", confirming = false, confirmingLabel = "Working...", additionalAction, onConfirm, onCancel }: ConfirmDialogProps) {
  const cancel = useRef<HTMLButtonElement>(null);
  return <Dialog open={open} title={title} description={description} role="alertdialog" onClose={onCancel}
    busy={confirming} initialFocusRef={cancel} showClose={false} dismissOnOutside
    actions={<><Button ref={cancel} type="button" variant="outline" disabled={confirming} onClick={onCancel}>{cancelLabel}</Button>
      <Button type="button" variant="destructive" disabled={confirming} onClick={onConfirm}>{confirming ? confirmingLabel : confirmLabel}</Button>{additionalAction}</>}>
    <p role="status" className="suite-sr-only">{confirming ? confirmingLabel : ""}</p>
    {error && <p role="alert" className="suite-field-error">{error}</p>}
  </Dialog>;
}
