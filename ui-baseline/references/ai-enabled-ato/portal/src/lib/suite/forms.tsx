import { useRef, type ComponentPropsWithRef, type FormEvent } from "react";
type Props = Omit<ComponentPropsWithRef<"form">, "onSubmit"> & {
  onSubmit?: (event: FormEvent<HTMLFormElement>) => void | Promise<unknown>;
};
/** Same native form/validation/DOM. Pending async handlers cannot be submitted twice. */
export function SuiteForm({ onSubmit, ...props }: Props) {
  const pending = useRef(false);
  function submit(event: FormEvent<HTMLFormElement>) {
    if (pending.current || props["aria-busy"] === true || props["aria-busy"] === "true") {
      event.preventDefault(); return;
    }
    pending.current = true;
    let result: void | Promise<unknown>;
    try { result = onSubmit?.(event); }
    catch (error) { pending.current = false; throw error; }
    if (result && typeof result.then === "function") {
      // Release the lock without consuming an unexpected rejection from the handler.
      return result.finally(() => { pending.current = false; });
    } else { pending.current = false; }
  }
  return <form {...props} onSubmit={submit} />;
}
