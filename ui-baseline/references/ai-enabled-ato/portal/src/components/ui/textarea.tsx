import * as React from "react";
import { cn } from "../../lib/utils";
import "./suite-components.css";

type TextareaProps = React.ComponentProps<"textarea"> & { variant?: "field" | "composer" };
export const Textarea = React.forwardRef<HTMLTextAreaElement, TextareaProps>(function Textarea({ className, variant = "field", ...props }, ref) {
  return <textarea {...props} ref={ref} className={cn(variant === "composer" ? "suite-composer-textarea" : "suite-textarea", className)} data-suite-component="textarea" data-variant={variant} />;
});
