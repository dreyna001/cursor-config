import * as React from "react";
import { Slot } from "@radix-ui/react-slot";
import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "../../lib/utils";
import "./suite-components.css";

export const buttonVariants = cva("suite-button", {
  variants: {
    variant: { default: "suite-button--primary", secondary: "suite-button--secondary", outline: "suite-button--outline", destructive: "suite-button--destructive", ghost: "suite-button--ghost", link: "suite-button--link" },
    size: { default: "suite-button--default", sm: "suite-button--sm", lg: "suite-button--lg", icon: "suite-button--icon" },
  },
  defaultVariants: { variant: "default", size: "default" },
});
export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement>, VariantProps<typeof buttonVariants> { asChild?: boolean; }
export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(function Button({ asChild = false, variant, size, className, ...props }, ref) {
  const Component = asChild ? Slot : "button";
  return <Component {...props} ref={ref} className={cn(buttonVariants({ variant, size }), className)} data-suite-component="button" />;
});
