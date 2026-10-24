import * as React from "react";
import { cn } from "../../lib/utils";
import "./suite-components.css";

export const Input = React.forwardRef<HTMLInputElement, React.ComponentProps<"input">>(function Input({ className, ...props }, ref) {
  return <input {...props} ref={ref} className={cn("suite-input", className)} data-suite-component="input" />;
});
