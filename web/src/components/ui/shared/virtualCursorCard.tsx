"use client";

import React, {
  useState,
  useRef,
  useEffect,
  ReactNode,
  forwardRef,
  useImperativeHandle,
  useCallback,
  CSSProperties,
  ElementType,
  HTMLAttributes,
} from "react";
import { createPortal } from "react-dom";
import { Placement } from "@floating-ui/react-dom";

type SpacingToken =
  | "0" | "1" | "2" | "4" | "6" | "8" | "12" | "16" | "20" | "24" | "32" | "40" | "48" | "56" | "64" | "80" | "96" | "128" | "160" | "192" | "224" | "256" | "320" | "384" | "448" | "512"
  | "xs" | "s" | "m" | "l" | "xl" | "2xl";

type Colors =
  | "brand-weak" | "brand-medium" | "brand-strong"
  | "accent-weak" | "accent-medium" | "accent-strong"
  | "neutral-weak" | "neutral-medium" | "neutral-strong"
  | "danger-weak" | "danger-medium" | "danger-strong"
  | "warning-weak" | "warning-medium" | "warning-strong"
  | "success-weak" | "success-medium" | "success-strong"
  | "info-weak" | "info-medium" | "info-strong";

type TextVariant = string;
type TextSize = "xs" | "s" | "m" | "l" | "xl" | "2xl";
type TextType = "default" | "mono" | "code";
type TextWeight = "default" | "medium" | "strong";
type RadiusSize = "none" | "xs" | "s" | "m" | "l" | "xl" | "full";
type RadiusNest = "top" | "right" | "bottom" | "left" | "top-left" | "top-right" | "bottom-right" | "bottom-left";
type ShadowSize = "xs" | "s" | "m" | "l" | "xl";
type flex = "1" | "auto" | "initial" | "none";
type opacity = 0 | 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 | 100;

interface ResponsiveProps extends HTMLAttributes<HTMLDivElement> {
  top?: SpacingToken;
  right?: SpacingToken;
  bottom?: SpacingToken;
  left?: SpacingToken;
  hide?: boolean;
  position?: CSSProperties["position"];
  overflow?: CSSProperties["overflow"];
  overflowX?: CSSProperties["overflowX"];
  overflowY?: CSSProperties["overflowY"];
  aspectRatio?: CSSProperties["aspectRatio"];
  style?: CSSProperties;
}

interface ResponsiveFlexProps extends ResponsiveProps {
  horizontal?: "start" | "center" | "end" | "between" | "around" | "even" | "stretch";
  vertical?: "start" | "center" | "end" | "between" | "around" | "even" | "stretch";
  center?: boolean;
  direction?: "row" | "column" | "row-reverse" | "column-reverse";
}

interface FlexProps extends HTMLAttributes<HTMLDivElement> {
  direction?: "row" | "column" | "row-reverse" | "column-reverse";
  horizontal?: "start" | "center" | "end" | "between" | "around" | "even" | "stretch";
  vertical?: "start" | "center" | "end" | "between" | "around" | "even" | "stretch";
  center?: boolean;
  wrap?: boolean;
  flex?: flex;
  xl?: ResponsiveFlexProps;
  l?: ResponsiveFlexProps;
  m?: ResponsiveFlexProps;
  s?: ResponsiveFlexProps;
  xs?: ResponsiveFlexProps;
}

interface SizeProps extends HTMLAttributes<HTMLDivElement> {
  width?: number | SpacingToken;
  height?: number | SpacingToken;
  maxWidth?: number | SpacingToken;
  minWidth?: number | SpacingToken;
  minHeight?: number | SpacingToken;
  maxHeight?: number | SpacingToken;
  fit?: boolean;
  fitWidth?: boolean;
  fitHeight?: boolean;
  fill?: boolean;
  fillWidth?: boolean;
  fillHeight?: boolean;
  aspectRatio?: CSSProperties["aspectRatio"];
}

interface SpacingProps extends HTMLAttributes<HTMLDivElement> {
  padding?: SpacingToken;
  paddingLeft?: SpacingToken;
  paddingRight?: SpacingToken;
  paddingTop?: SpacingToken;
  paddingBottom?: SpacingToken;
  paddingX?: SpacingToken;
  paddingY?: SpacingToken;
  margin?: SpacingToken;
  marginLeft?: SpacingToken;
  marginRight?: SpacingToken;
  marginTop?: SpacingToken;
  marginBottom?: SpacingToken;
  marginX?: SpacingToken;
  marginY?: SpacingToken;
  gap?: SpacingToken | "-1";
  top?: SpacingToken;
  right?: SpacingToken;
  bottom?: SpacingToken;
  left?: SpacingToken;
}

interface StyleProps extends HTMLAttributes<HTMLDivElement> {
  textVariant?: TextVariant;
  textSize?: TextSize;
  textType?: TextType;
  textWeight?: TextWeight;
  background?: Colors | "surface" | "overlay" | "page" | "transparent";
  solid?: Colors;
  borderTop?: Colors | "surface" | "transparent";
  borderRight?: Colors | "surface" | "transparent";
  borderBottom?: Colors | "surface" | "transparent";
  borderLeft?: Colors | "surface" | "transparent";
  borderX?: Colors | "surface" | "transparent";
  borderY?: Colors | "surface" | "transparent";
  border?: Colors | "surface" | "transparent";
  borderStyle?: "solid" | "dashed";
  borderWidth?: 1 | 2 | 4 | 6 | 8;
  topRadius?: RadiusSize;
  rightRadius?: RadiusSize;
  bottomRadius?: RadiusSize;
  leftRadius?: RadiusSize;
  topLeftRadius?: RadiusSize;
  topRightRadius?: RadiusSize;
  bottomLeftRadius?: RadiusSize;
  bottomRightRadius?: RadiusSize;
  radius?: RadiusSize | `${RadiusSize}-${RadiusNest}`;
  shadow?: ShadowSize;
  cursor?: CSSProperties["cursor"] | "interactive" | ReactNode;
}

interface DisplayProps extends HTMLAttributes<HTMLDivElement> {
  as?: ElementType;
  inline?: boolean;
  hide?: boolean;
  pointerEvents?: "none" | "all" | "auto";
  position?: CSSProperties["position"];
  overflow?: CSSProperties["overflow"];
  overflowX?: CSSProperties["overflowX"];
  overflowY?: CSSProperties["overflowY"];
  transition?: "micro-short" | "micro-medium" | "micro-long" | "macro-short" | "macro-medium" | "macro-long";
  opacity?: opacity;
  zIndex?: -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10;
  dark?: boolean;
  light?: boolean;
}

interface CommonProps extends HTMLAttributes<HTMLDivElement> {
  onBackground?: Colors;
  onSolid?: Colors;
  align?: CSSProperties["textAlign"];
  className?: string;
  children?: ReactNode;
  style?: React.CSSProperties;
}

// Flex component interface
interface FlexComponentProps extends FlexProps, StyleProps, SpacingProps, SizeProps, CommonProps, DisplayProps {
  xl?: ResponsiveFlexProps;
  l?: ResponsiveFlexProps;
  m?: ResponsiveFlexProps;
  s?: ResponsiveFlexProps;
  xs?: ResponsiveFlexProps;
}

// Basic Flex component implementation
const Flex = forwardRef<HTMLDivElement, FlexComponentProps>(
  ({ children, className, style, as: Component = "div", ...props }, ref) => {
    return (
      <Component
        ref={ref}
        className={className}
        style={style}
        {...props}
      >
        {children}
      </Component>
    );
  }
);

Flex.displayName = "Flex";

export interface VirtualCursorCardProps extends React.ComponentProps<typeof Flex> {
  trigger?: ReactNode;
  overlay?: ReactNode;
  placement?: Placement;
  className?: string;
  style?: React.CSSProperties;
}

const VirtualCursorCard = forwardRef<HTMLDivElement, VirtualCursorCardProps>(
  ({ trigger, overlay, placement = "bottom-left", className, style, ...flex }, ref) => {
    const [isHovering, setIsHovering] = useState(false);
    const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });
    const [isTouchDevice, setIsTouchDevice] = useState(false);
    const cardRef = useRef<HTMLDivElement | null>(null);
    const triggerRef = useRef<HTMLDivElement | null>(null);

    useImperativeHandle(ref, () => cardRef.current as HTMLDivElement);

    useEffect(() => {
      const checkTouchDevice = () => {
        return "ontouchstart" in window;
      };

      setIsTouchDevice(checkTouchDevice());
    }, []);

    const handleMouseMove = useCallback(
      (e: MouseEvent) => {
        if (isHovering && !isTouchDevice) {
          setMousePosition({ x: e.clientX, y: e.clientY });
        }
      },
      [isHovering, isTouchDevice],
    );

    useEffect(() => {
      if (!isTouchDevice) {
        document.addEventListener("mousemove", handleMouseMove);

        return () => {
          document.removeEventListener("mousemove", handleMouseMove);
        };
      }
      return undefined;
    }, [handleMouseMove, isTouchDevice]);

    // Create a portal container if it doesn't exist
    useEffect(() => {
      if (typeof document !== "undefined") {
        let portalContainer = document.getElementById("cursor-card-portal");
        if (!portalContainer) {
          portalContainer = document.createElement("div");
          portalContainer.id = "cursor-card-portal";
          document.body.appendChild(portalContainer);
        }
      }

      return () => {
        if (typeof document !== "undefined") {
          const portalContainer = document.getElementById("cursor-card-portal");
          if (portalContainer && portalContainer.childNodes.length === 0) {
            document.body.removeChild(portalContainer);
          }
        }
      };
    }, []);

    return (
      <>
        <style jsx>{`
          .fadeIn {
            animation: fadeIn 0.2s ease-in-out;
          }

          @keyframes fadeIn {
            from {
              opacity: 0;
            }
            to {
              opacity: 1;
            }
          }
        `}</style>
        {trigger && (
          <Flex
            ref={triggerRef}
            onMouseEnter={() => !isTouchDevice && setIsHovering(true)}
            onMouseLeave={() => !isTouchDevice && setIsHovering(false)}
          >
            {trigger}
          </Flex>
        )}
        {isHovering &&
          !isTouchDevice &&
          typeof document !== "undefined" &&
          createPortal(
            <Flex
              zIndex={10}
              position="fixed"
              top="0"
              left="0"
              pointerEvents="none"
              ref={cardRef}
              className={`fadeIn ${className || ""}`}
              style={{
                isolation: "isolate",
                transform: `translate(calc(${mousePosition.x}px ${placement.includes("left") ? "- 100%" : placement.includes("right") ? "" : "- 50%"}), calc(${mousePosition.y}px ${placement.includes("top") ? "- 100%" : placement.includes("bottom") ? "" : "- 50%"}))`,
                ...style,
              }}
              {...flex}
            >
              {overlay}
            </Flex>,
            document.getElementById("cursor-card-portal") || document.body,
          )}
      </>
    );
  },
);

VirtualCursorCard.displayName = "VirtualCursorCard";

export { VirtualCursorCard };
