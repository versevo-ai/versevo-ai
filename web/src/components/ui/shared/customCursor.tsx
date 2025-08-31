/* eslint-disable @typescript-eslint/no-unused-vars */
"use client";

import { motion, useSpring } from "motion/react";
import { FC, JSX, useEffect, useRef, useState } from "react";

interface Position {
  x: number;
  y: number;
}

export interface CustomCursorProps {
  cursor?: JSX.Element;
  springConfig?: {
    damping: number;
    stiffness: number;
    mass: number;
    restDelta: number;
  };
}

interface DynamicCursorProps {
  isOverText: boolean;
  textSize?: number;
}

const DynamicCursorSVG: FC<DynamicCursorProps> = ({ isOverText, textSize = 16 }) => {
  // Calculate caret height and width based on text size
  const caretHeight = Math.max(1, Math.min(512, textSize * 1.2));
  const caretWidth = Math.max(2, Math.min(4, textSize * 4));
  const fillColor = "rgba(82, 151, 255, 1)";

  if (isOverText) {
    // Text caret - simple rounded vertical bar
    return (
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width={caretWidth + 2}
        height={caretHeight}
        viewBox={`0 0 ${caretWidth + 2} ${caretHeight}`}
        fill="none"
        style={{ scale: 1 }}
      >
        {/* Main caret body - rounded vertical bar */}
        <rect
          width={caretWidth}
          height={caretHeight}
          x={1}
          y={0}
          fill={fillColor}
          rx={caretWidth / 2}
        />
        <rect
          width={caretWidth}
          height={caretHeight}
          x={1}
          y={0}
          rx={caretWidth / 2}
        />
      </svg>
    );
  }

  // Default cursor
  return (
    <div className="relative">
      {/* Rainbow glow layers - multiple layers for enhanced effect */}
      <div
        className="absolute inset-0 z-0 opacity-40 animate-rainbow"
        style={{
          background: 'linear-gradient(90deg, var(--color-1), var(--color-5), var(--color-3), var(--color-4), var(--color-2))',
          backgroundSize: '400% 100%',
          maskImage: `url("data:image/svg+xml,${encodeURIComponent(`
            <svg xmlns="http://www.w3.org/2000/svg" width="50" height="54" viewBox="0 0 50 54">
              <path d="M43.7146 40.6933L28.5431 6.34306C27.3556 3.65428 23.5772 3.69516 22.3668 6.32755L6.57226 40.6778C5.3134 43.4156 7.97238 46.298 10.803 45.2549L24.7662 40.109C25.0221 40.0147 25.2999 40.0156 25.5494 40.1082L39.4193 45.254C42.2261 46.2953 44.9254 43.4347 43.7146 40.6933Z" stroke="white" stroke-width="8" fill="none"/>
            </svg>
          `)}")`,
          maskSize: 'contain',
          maskRepeat: 'no-repeat',
          maskPosition: 'center',
          transform: 'scale(0.5)',
          filter: 'blur(4px)',
          animationDuration: '3s',
        }}
      />

      {/* Second glow layer */}
      <div
        className="absolute inset-0 z-0 opacity-30 animate-rainbow"
        style={{
          background: 'linear-gradient(45deg, var(--color-2), var(--color-1), var(--color-5), var(--color-3), var(--color-4))',
          backgroundSize: '600% 100%',
          maskImage: `url("data:image/svg+xml,${encodeURIComponent(`
            <svg xmlns="http://www.w3.org/2000/svg" width="50" height="54" viewBox="0 0 50 54">
              <path d="M43.7146 40.6933L28.5431 6.34306C27.3556 3.65428 23.5772 3.69516 22.3668 6.32755L6.57226 40.6778C5.3134 43.4156 7.97238 46.298 10.803 45.2549L24.7662 40.109C25.0221 40.0147 25.2999 40.0156 25.5494 40.1082L39.4193 45.254C42.2261 46.2953 44.9254 43.4347 43.7146 40.6933Z" stroke="white" stroke-width="12" fill="none"/>
            </svg>
          `)}")`,
          maskSize: 'contain',
          maskRepeat: 'no-repeat',
          maskPosition: 'center',
          transform: 'scale(0.5)',
          filter: 'blur(8px)',
          animationDuration: '4s',
          animationDirection: 'reverse',
        }}
      />

      {/* Third outer glow layer */}
      <div
        className="absolute inset-0 z-0 opacity-20 animate-rainbow"
        style={{
          background: 'linear-gradient(135deg, var(--color-4), var(--color-2), var(--color-1), var(--color-5), var(--color-3))',
          backgroundSize: '800% 100%',
          maskImage: `url("data:image/svg+xml,${encodeURIComponent(`
            <svg xmlns="http://www.w3.org/2000/svg" width="50" height="54" viewBox="0 0 50 54">
              <path d="M43.7146 40.6933L28.5431 6.34306C27.3556 3.65428 23.5772 3.69516 22.3668 6.32755L6.57226 40.6778C5.3134 43.4156 7.97238 46.298 10.803 45.2549L24.7662 40.109C25.0221 40.0147 25.2999 40.0156 25.5494 40.1082L39.4193 45.254C42.2261 46.2953 44.9254 43.4347 43.7146 40.6933Z" stroke="white" stroke-width="16" fill="none"/>
            </svg>
          `)}")`,
          maskSize: 'contain',
          maskRepeat: 'no-repeat',
          maskPosition: 'center',
          transform: 'scale(0.5)',
          filter: 'blur(12px)',
          animationDuration: '5s',
        }}
      />

      {/* Main animated rainbow border */}
      <div
        className="absolute inset-0 z-0 animate-rainbow"
        style={{
          background: 'linear-gradient(90deg, var(--color-1), var(--color-5), var(--color-3), var(--color-4), var(--color-2))',
          backgroundSize: '300% 100%',
          maskImage: `url("data:image/svg+xml,${encodeURIComponent(`
            <svg xmlns="http://www.w3.org/2000/svg" width="50" height="54" viewBox="0 0 50 54">
              <path d="M43.7146 40.6933L28.5431 6.34306C27.3556 3.65428 23.5772 3.69516 22.3668 6.32755L6.57226 40.6778C5.3134 43.4156 7.97238 46.298 10.803 45.2549L24.7662 40.109C25.0221 40.0147 25.2999 40.0156 25.5494 40.1082L39.4193 45.254C42.2261 46.2953 44.9254 43.4347 43.7146 40.6933Z" stroke="white" stroke-width="4" fill="none"/>
            </svg>
          `)}")`,
          maskSize: 'contain',
          maskRepeat: 'no-repeat',
          maskPosition: 'center',
          transform: 'scale(0.5)',
          animationDuration: '2s',
        }}
      />

      <svg
        xmlns="http://www.w3.org/2000/svg"
        width={50}
        height={54}
        viewBox="0 0 50 54"
        fill="none"
        style={{ scale: 0.5 }}
        className="relative z-10"
      >
        <defs>
          <filter
            id="filter0_d_91_7928"
            x={0.602397}
            y={0.952444}
            width={49.0584}
            height={52.428}
            filterUnits="userSpaceOnUse"
            colorInterpolationFilters="sRGB"
          >
            <feFlood floodOpacity={0} result="BackgroundImageFix" />
            <feColorMatrix
              in="SourceAlpha"
              type="matrix"
              values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
              result="hardAlpha"
            />
            <feOffset dy={2.25825} />
            <feGaussianBlur stdDeviation={2.25825} />
            <feComposite in2="hardAlpha" operator="out" />
            <feColorMatrix
              type="matrix"
              values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.08 0"
            />
            <feBlend
              mode="normal"
              in2="BackgroundImageFix"
              result="effect1_dropShadow_91_7928"
            />
            <feBlend
              mode="normal"
              in="SourceGraphic"
              in2="effect1_dropShadow_91_7928"
              result="shape"
            />
          </filter>
        </defs>

        {/* Main cursor body */}
        <g filter="url(#filter0_d_91_7928)">
          <path
            d="M42.6817 41.1495L27.5103 6.79925C26.7269 5.02557 24.2082 5.02558 23.3927 6.79925L7.59814 41.1495C6.75833 42.9759 8.52712 44.8902 10.4125 44.1954L24.3757 39.0496C24.8829 38.8627 25.4385 38.8627 25.9422 39.0496L39.8121 44.1954C41.6849 44.8902 43.4884 42.9759 42.6817 41.1495Z"
            fill="rgba(7, 62, 121, 1)"
          />
          <path
            d="M43.7146 40.6933L28.5431 6.34306C27.3556 3.65428 23.5772 3.69516 22.3668 6.32755L6.57226 40.6778C5.3134 43.4156 7.97238 46.298 10.803 45.2549L24.7662 40.109C25.0221 40.0147 25.2999 40.0156 25.5494 40.1082L39.4193 45.254C42.2261 46.2953 44.9254 43.4347 43.7146 40.6933Z"
            stroke="white"
            strokeWidth={2.25825}
          />
        </g>
      </svg>
    </div>
  );
};

export function CustomCursor({
  cursor,
  springConfig = {
    damping: 45,
    stiffness: 400,
    mass: 1,
    restDelta: 0.001,
  },
}: CustomCursorProps) {
  const [isMoving, setIsMoving] = useState(false);
  const [isOverText, setIsOverText] = useState(false);
  const [textSize, setTextSize] = useState(16);
  const [isInitialized, setIsInitialized] = useState(false);
  const lastMousePos = useRef<Position>({ x: 0, y: 0 });
  const velocity = useRef<Position>({ x: 0, y: 0 });
  const lastUpdateTime = useRef(Date.now());
  const previousAngle = useRef(0);
  const accumulatedRotation = useRef(0);

  const cursorX = useSpring(0, springConfig);
  const cursorY = useSpring(0, springConfig);
  const rotation = useSpring(0, {
    ...springConfig,
    damping: 60,
    stiffness: 300,
  });
  const scale = useSpring(1, {
    ...springConfig,
    stiffness: 500,
    damping: 35,
  });

  useEffect(() => {
    const updateVelocity = (currentPos: Position) => {
      const currentTime = Date.now();
      const deltaTime = currentTime - lastUpdateTime.current;

      if (deltaTime > 0) {
        velocity.current = {
          x: (currentPos.x - lastMousePos.current.x) / deltaTime,
          y: (currentPos.y - lastMousePos.current.y) / deltaTime,
        };
      }

      lastUpdateTime.current = currentTime;
      lastMousePos.current = currentPos;
    };

    const checkTextElement = (element: Element | null): boolean => {
      if (!element || !isInitialized) return false;

      const tagName = element.tagName;

      // Only show caret for actual text input fields
      if (tagName === 'INPUT' || tagName === 'TEXTAREA') {
        const input = element as HTMLInputElement | HTMLTextAreaElement;
        // Only show caret for text inputs, not buttons or other input types
        if (tagName === 'INPUT') {
          const inputType = (input as HTMLInputElement).type;
          return ['text', 'email', 'password', 'search', 'url', 'tel'].includes(inputType);
        }
        return true;
      }

      // For content editable elements
      if (element.hasAttribute('contenteditable') &&
          element.getAttribute('contenteditable') !== 'false') {
        return true;
      }

      // Only consider very specific text elements that are clearly meant for text selection
      const selectableTextTags = ['P', 'SPAN', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'A', 'LI', 'TD', 'TH', 'LABEL', 'INPUT', 'TEXTAREA'];
      if (selectableTextTags.includes(tagName)) {
        const computedStyle = window.getComputedStyle(element);

        // Additional checks to ensure it's actually selectable text
        const userSelect = computedStyle.userSelect;
        const cursor = computedStyle.cursor;
        const display = computedStyle.display;

        // Must explicitly allow text selection
        if (userSelect === 'text' || cursor === 'text') {
          return true;
        }

        // Check if it's a pure text element (not a container)
        if (userSelect !== 'none' &&
            element.textContent &&
            element.textContent.trim().length > 0 &&
            element.children.length === 0 && // No child elements
            display !== 'flex' &&
            display !== 'grid' &&
            !element.classList.contains('cursor-pointer') &&
            !(element as HTMLElement).onclick &&
            !element.getAttribute('role')) {

          // Additional check: ensure it's not too large (likely a container)
          const rect = element.getBoundingClientRect();
          if (rect.width < window.innerWidth * 0.8 && rect.height < 200) {
            return true;
          }
        }
      }

      return false;
    };

    const getTextSize = (element: Element): number => {
      const computedStyle = window.getComputedStyle(element);
      const fontSize = computedStyle.fontSize;
      return parseInt(fontSize, 10) || 16;
    };

    const smoothMouseMove = (e: MouseEvent) => {
      const currentPos = { x: e.clientX, y: e.clientY };
      updateVelocity(currentPos);

      // Initialize on first mouse move
      if (!isInitialized) {
        setIsInitialized(true);
        setIsOverText(false); // Ensure we start with cursor, not caret
      }

      // Text detection logic
      const elementUnderCursor = document.elementFromPoint(e.clientX, e.clientY);
      const isText = checkTextElement(elementUnderCursor);

      setIsOverText(isText);

      if (isText && elementUnderCursor) {
        const size = getTextSize(elementUnderCursor);
        setTextSize(size);
      }

      const speed = Math.sqrt(
        Math.pow(velocity.current.x, 2) + Math.pow(velocity.current.y, 2),
      );

      cursorX.set(currentPos.x);
      cursorY.set(currentPos.y);

      // Only apply rotation when not over text (caret shouldn't rotate)
      if (speed > 0.1 && !isText) {
        const currentAngle =
          Math.atan2(velocity.current.y, velocity.current.x) * (180 / Math.PI) +
          90;

        let angleDiff = currentAngle - previousAngle.current;
        if (angleDiff > 180) angleDiff -= 360;
        if (angleDiff < -180) angleDiff += 360;
        accumulatedRotation.current += angleDiff;
        rotation.set(accumulatedRotation.current);
        previousAngle.current = currentAngle;

        scale.set(0.95);
        setIsMoving(true);

        setTimeout(() => {
          scale.set(1);
          setIsMoving(false);
        }, 150);
      } else if (isText) {
        // Reset rotation for text caret
        rotation.set(0);
        scale.set(1);
      }
    };

    let rafId: number;
    const throttledMouseMove = (e: MouseEvent) => {
      if (rafId) return;

      rafId = requestAnimationFrame(() => {
        smoothMouseMove(e);
        rafId = 0;
      });
    };

    document.body.style.cursor = "none";
    window.addEventListener("mousemove", throttledMouseMove);

    return () => {
      window.removeEventListener("mousemove", throttledMouseMove);
      document.body.style.cursor = "auto";
      if (rafId) cancelAnimationFrame(rafId);
    };
  }, [cursorX, cursorY, rotation, scale, isInitialized]);

  return (
    <motion.div
      style={{
        position: "fixed",
        left: cursorX,
        top: cursorY,
        translateX: "-50%",
        translateY: "-50%",
        rotate: rotation,
        scale: scale,
        zIndex: 100,
        pointerEvents: "none",
        willChange: "transform",
        opacity: isInitialized ? 1 : 0,
      }}
      initial={{ scale: 0, opacity: 0 }}
      animate={{ scale: isInitialized ? 1 : 0, opacity: isInitialized ? 1 : 0 }}
      transition={{
        type: "spring",
        stiffness: 400,
        damping: 30,
      }}
    >
      {cursor || <DynamicCursorSVG isOverText={isOverText} textSize={textSize} />}
    </motion.div>
  );
}
