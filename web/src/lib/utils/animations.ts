import { type Variants } from 'framer-motion';

export const fadeInUp = (delay = 0): Variants => ({
  initial: {
    opacity: 0,
    y: 20
  },
  animate: {
    opacity: 1,
    y: 0,
    transition: {
      duration: 0.5,
      delay,
      ease: 'easeOut',
    },
  },
});

export const fadeInDown = (delay = 0): Variants => ({
  initial: {
    opacity: 0,
    y: -20
  },
  animate: {
    opacity: 1,
    y: 0,
    transition: {
      duration: 0.5,
      delay,
      ease: 'easeOut',
    },
  },
});

export const scaleIn = (delay = 0): Variants => ({
  initial: {
    opacity: 0,
    scale: 0.8
  },
  animate: {
    opacity: 1,
    scale: 1,
    transition: {
      duration: 0.3,
      delay,
      ease: 'easeOut',
    },
  },
});

export const staggerContainer = (staggerChildren = 0.1): Variants => ({
  animate: {
    transition: {
      staggerChildren,
    },
  },
});

export const hoverScale = {
  whileHover: { scale: 1.05 },
  whileTap: { scale: 0.95 },
};
