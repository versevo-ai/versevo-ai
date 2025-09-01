import { ComponentPropsWithoutRef, CSSProperties, FC } from "react";

import { cn } from "@/lib/utils";

export interface ShinyTextBoxProps extends ComponentPropsWithoutRef<"span"> {
  shimmerWidth?: number;
}

export const ShinyTextBox: FC<ShinyTextBoxProps> = ({
  children,
  className,
  shimmerWidth = 100,
  ...props
}) => {
  return (
    <span
      style={
        {
          "--shiny-width": `${shimmerWidth}px`,
          animation: "shiny-text 2s ease-in-out infinite",
        } as CSSProperties
      }
      className={cn(
        "mx-auto max-w-md text-[#073E79]/70 dark:text-[#073E79]/80",

        // Shine effect
        "bg-clip-text bg-no-repeat [background-position:-100%_0] [background-size:var(--shiny-width)_100%]",

        // Shine gradient - updated to match website colors
        "bg-gradient-to-r from-transparent via-[#073E79]/80 via-50% to-transparent dark:via-[#073E79]/90",

        // Prevent clickable cursor
        "cursor-default",

        // Prevent system cursor and let parent handle cursor
        "cursor-none",

        className,
      )}
      {...props}
    >
      {children}
      <style jsx>{`
        @keyframes shiny-text {
          0% {
            background-position: -100% 0;
          }
          100% {
            background-position: 200% 0;
          }
        }
      `}</style>
    </span>
  );
};
