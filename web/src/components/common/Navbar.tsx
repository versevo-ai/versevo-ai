'use client';

import React from 'react';
import Image from 'next/image';
import { motion } from 'framer-motion';
import { Logo } from '@public/shared';
import { type NavbarProps } from '@/lib/types';
import { COMPANY_INFO } from '@/lib/constants';
import { fadeInDown, hoverScale } from '@/lib/utils/animations';
import { cn } from '@/lib/utils';

const Navbar: React.FC<NavbarProps> = ({ className }) => {
  return (
    <motion.nav
      variants={fadeInDown()}
      initial="initial"
      animate="animate"
      className={cn(
        'flex items-center justify-center gap-x-2 sm:gap-x-3',
        'bg-[#B2E2F0] rounded-[15px] sm:rounded-[20px] md:rounded-[25px]',
        'px-3 sm:px-4 md:px-6 py-2 sm:py-3 md:py-4',
        'shadow-md mt-2 sm:mt-4 md:mt-8 mx-auto',
        'min-w-[250px] min-h-[60px]',
        className
      )}
      style={{
        width: 'min(382.8px, 90vw)',
        height: 'min(100px, 12vh)',
      }}
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
