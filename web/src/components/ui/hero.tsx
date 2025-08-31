'use client';

import React from 'react';
import { motion } from 'framer-motion';
import Navbar from '@/components/common/Navbar';
import { AvatarRow } from '@/components/ui/landing/AvatarRow';
import { type HeroProps } from '@/lib/types';
import { COMPANY_INFO, ANIMATION_DELAYS } from '@/lib/constants';
import { fadeInUp, fadeInDown } from '@/lib/utils/animations';
import { cn } from '@/lib/utils';

const Hero: React.FC<HeroProps> = ({ className, children }) => {
  return (
    <div 
      className={cn(
        'h-screen overflow-y-auto w-full flex flex-col',
        'bg-gradient-to-br from-blue-500 via-blue-300 to-cyan-200',
        className
      )}
    >
      <motion.div
        variants={fadeInDown()}
        initial="initial"
        animate="animate"
        className="flex items-center justify-center"
      >
        <Navbar />
      </motion.div>

      <div className="flex-grow flex items-center justify-center">
        <div className="max-w-3xl mx-auto py-16 px-4 text-center">
          <motion.h1
            variants={fadeInUp(ANIMATION_DELAYS.HERO_TITLE)}
            initial="initial"
            animate="animate"
            className="text-6xl text-[#073E79] mb-4"
          >
            The <span className="text-[#073E79] font-bold">Ultimate</span>
            <br />
            {COMPANY_INFO.TAGLINE.split(' ').slice(-3).join(' ')}
          </motion.h1>

          <motion.p
            variants={fadeInUp(ANIMATION_DELAYS.HERO_DESCRIPTION)}
            initial="initial"
            animate="animate"
            className="text-[#073E79] mb-12 font-normal max-w-2xl mx-auto"
          >
            {COMPANY_INFO.DESCRIPTION}
          </motion.p>

          <motion.p
            variants={fadeInUp(ANIMATION_DELAYS.HERO_TEAM_INFO)}
            initial="initial"
            animate="animate"
            className="text-[#073E79] mb-6 font-semibold max-w-2xl mx-auto"
          >
            {COMPANY_INFO.ORIGIN}
          </motion.p>

          <motion.div
            variants={fadeInUp(ANIMATION_DELAYS.HERO_AVATARS)}
            initial="initial"
            animate="animate"
            className="mb-12 flex justify-center"
          >
            <AvatarRow size="sm" />
          </motion.div>

          {children && (
            <motion.div
              variants={fadeInUp(ANIMATION_DELAYS.HERO_AVATARS + 0.1)}
              initial="initial"
              animate="animate"
              className="flex-grow flex items-center justify-center max-w-md mx-auto my-auto"
            >
              {children}
            </motion.div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Hero;
