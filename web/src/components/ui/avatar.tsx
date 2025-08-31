'use client';

import * as React from 'react';
import Image from 'next/image';
import { cn } from '@/lib/utils';

interface AvatarProps {
  className?: string;
  children?: React.ReactNode;
}

interface AvatarImageProps {
  src?: string;
  alt?: string;
  className?: string;
  width?: number;
  height?: number;
}

interface AvatarFallbackProps {
  className?: string;
  children?: React.ReactNode;
}

const Avatar = React.forwardRef<HTMLDivElement, AvatarProps>(
  ({ className, children, ...props }, ref) => (
    <div
      ref={ref}
      className={cn(
        'relative flex h-10 w-10 shrink-0 overflow-hidden rounded-full',
        'shadow-lg',
        className
      )}
      style={{
        filter: 'drop-shadow(0px 4px 4px rgba(21, 101, 239, 0.7))',
      }}
      {...props}
    >
      {children}
    </div>
  )
);
Avatar.displayName = 'Avatar';

const AvatarImage = React.forwardRef<HTMLImageElement, AvatarImageProps>(
  ({ className, src, alt = '', width = 100, height = 100, ...props }, ref) => {
    const [imageError, setImageError] = React.useState(false);
    const [imageLoaded, setImageLoaded] = React.useState(false);

    const handleError = React.useCallback(() => {
      setImageError(true);
    }, []);

    const handleLoad = React.useCallback(() => {
      setImageLoaded(true);
    }, []);

    const handleContextMenu = React.useCallback((e: React.MouseEvent) => {
      e.preventDefault();
    }, []);

    const handleDragStart = React.useCallback((e: React.DragEvent) => {
      e.preventDefault();
    }, []);

    if (!src || imageError) {
      return null;
    }

    return (
      <Image
        ref={ref}
        src={src}
        alt={alt}
        width={width}
        height={height}
        className={cn(
          'aspect-square h-full w-full object-cover rounded-full',
          'transition-opacity duration-300',
          imageLoaded ? 'opacity-100' : 'opacity-0',
          className
        )}
        onError={handleError}
        onLoad={handleLoad}
        onContextMenu={handleContextMenu}
        onDragStart={handleDragStart}
        draggable={false}
        {...props}
      />
    );
  }
);
AvatarImage.displayName = 'AvatarImage';

const AvatarFallback = React.forwardRef<HTMLDivElement, AvatarFallbackProps>(
  ({ className, children, ...props }, ref) => (
    <div
      ref={ref}
      className={cn(
        'flex h-full w-full items-center justify-center rounded-full',
        'bg-gradient-to-br from-blue-400 to-blue-600',
        'text-white font-semibold text-sm',
        'select-none',
        className
      )}
      {...props}
    >
      {children}
    </div>
  )
);
AvatarFallback.displayName = 'AvatarFallback';

export { Avatar, AvatarImage, AvatarFallback };
