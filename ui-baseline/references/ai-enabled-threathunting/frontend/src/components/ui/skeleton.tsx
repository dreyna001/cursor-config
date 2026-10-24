import "./suite-components.css";
import { cn } from "../../lib/utils";

type SkeletonProps = React.HTMLAttributes<HTMLDivElement>;

export function Skeleton({ className, ...props }: SkeletonProps) {
  return (
    <div
      className={cn("suite-skeleton animate-pulse rounded-md bg-muted", className)}
      {...props}
    />
  );
}
