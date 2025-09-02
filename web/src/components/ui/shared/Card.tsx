'use client';

import { forwardRef } from 'react';
import { cn } from '@/src/lib/utils';
import { BaseComponentProps } from '@/lib/types';

interface CardProps extends BaseComponentProps {
  direction?: 'row' | 'column';
  radius?: string;
  border?: string;
  maxWidth?: number;
}

const Card = forwardRef<HTMLDivElement, CardProps>((
  { className, children, direction = 'column', radius = 'l-4', border = 'neutral-alpha-medium', maxWidth = 24, ...props },
  ref
) => {
  return (
    <div
      ref={ref}
      className={cn(
        'flex',
        `flex-${direction}`,
        `rounded-${radius}`,
        `border-${border}`,
        `max-w-${maxWidth}`,
        className
      )}
      {...props}
    >
      {children}
    </div>
  );
});

Card.displayName = 'Card';

export { Card };
