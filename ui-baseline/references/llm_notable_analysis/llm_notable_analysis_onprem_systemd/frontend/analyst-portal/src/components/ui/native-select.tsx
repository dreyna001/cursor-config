import * as React from "react";
import { cn } from "../../lib/utils";
import "./suite-components.css";

export const NativeSelect = React.forwardRef<HTMLSelectElement, React.ComponentProps<"select">>(function NativeSelect({ className, ...props }, ref) {
  return <select {...props} ref={ref} className={cn("suite-native-select", className)} data-suite-component="native-select" />;
});
