import * as React from "react";
import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "../../lib/utils";
import "./suite-components.css";

export const badgeVariants = cva("suite-badge", {
  variants: { variant: { default: "suite-badge--info", info: "suite-badge--info", neutral: "suite-badge--secondary", secondary: "suite-badge--secondary", outline: "suite-badge--outline", error: "suite-badge--destructive", destructive: "suite-badge--destructive", success: "suite-badge--success", warning: "suite-badge--warning", muted: "suite-badge--muted" } },
  defaultVariants: { variant: "default" },
});
export interface BadgeProps extends React.HTMLAttributes<HTMLDivElement>, VariantProps<typeof badgeVariants> { dot?: boolean; }
export function Badge({ className, variant, dot = false, ...props }: BadgeProps) {
  return <div {...props} className={cn(badgeVariants({ variant }), className)} data-suite-component="badge" data-dot={dot || undefined} />;
}
