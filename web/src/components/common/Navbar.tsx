'use client';

import React from 'react';
import Image from 'next/image';
import { motion } from 'framer-motion';
import { Logo } from '@/public/shared';
import { type NavbarProps } from '@/lib/types';
import { COMPANY_INFO } from '@/lib/constants';
import { fadeInDown, hoverScale } from '@/lib/utils/animations';
import { cn } from '@/src/lib/utils';

const Navbar: React.FC<NavbarProps> = ({ className }) => {
  return (
    <motion.nav
      variants={fadeInDown()}
      initial="initial"
      animate="animate"
      className={cn(
        'flex items-center justify-center gap-x-2 sm:gap-x-3',
        'mt-2 sm:mt-4 md:mt-8 mx-auto',
        className
      )}
    >
      <motion.div {...hoverScale}>
        <Image
          src={Logo}
          alt="Versevo Logo"
          width={32}
          height={36}
          className="w-5 h-6 sm:w-6 sm:h-7 md:w-8 md:h-9"
          draggable={false}
          onContextMenu={(e: React.MouseEvent<HTMLImageElement>) => e.preventDefault()}
          onDragStart={(e: React.DragEvent<HTMLImageElement>) => e.preventDefault()}
          priority
        />
      </motion.div>

      <motion.h1
        className="font-semibold text-blue-900 whitespace-nowrap"
        style={{
          fontSize: 'clamp(1rem, 4vw, 1.5rem)',
          lineHeight: '1.2',
        }}
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2, duration: 0.5 }}
      >
        {COMPANY_INFO.NAME.slice(0, -2)}
        <span className="font-bold">{COMPANY_INFO.NAME.slice(-2)}</span>
      </motion.h1>
    </motion.nav>
  );
};

export default Navbar;
