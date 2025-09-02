/* eslint-disable @typescript-eslint/no-empty-object-type */
// Common types and interfaces for the application

export interface BaseComponentProps {
  className?: string;
  children?: React.ReactNode;
}

export interface TeamMember {
  readonly name: string;
  readonly image: string;
  readonly alt: string;
  readonly fallback: string;
  readonly gitHubProfile: string;
}

export interface AvatarProps extends BaseComponentProps {
  size?: 'sm' | 'md' | 'lg';
}

export interface NavbarProps extends BaseComponentProps {
  // For future
}

export interface HeroProps extends BaseComponentProps {
  // For future
}

// Animation-related types
export interface MotionVariants {
  initial: Record<string, unknown>;
  animate: Record<string, unknown>;
  transition?: Record<string, unknown>;
}

// Layout-related types
export interface LayoutProps {
  children: React.ReactNode;
}

export interface MetadataConfig {
  title: string;
  description: string;
  keywords: string[];
  ogImage: string;
}
