/* eslint-disable @typescript-eslint/no-unused-vars */
'use client';

import React from 'react';
import { motion } from 'framer-motion';
import Navbar from '@/components/common/Navbar';
import { HeroBackground } from '@/public/hero';
import { AvatarRow } from '@/components/ui/landing/avatarRow';
import { Particles } from '@/components/ui/shared/particles';
import { ShinyTextBox } from './shared/shinyTextBox';
import { type HeroProps } from '@/lib/types';
import { COMPANY_INFO, ANIMATION_DELAYS } from '@/lib/constants';
import { fadeInUp, fadeInDown } from '@/lib/utils/animations';
import { cn } from '@/lib/utils';

const Hero: React.FC<HeroProps> = ({ className, children }) => {
  return (
    <div
      className={cn(
        'h-screen overflow-y-auto w-full flex flex-col',
        className
      )}
      style={{
        backgroundImage: `url(${HeroBackground.src})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat'
      }}
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
          <motion.div
            variants={fadeInUp(ANIMATION_DELAYS.HERO_TITLE)}
            initial="initial"
            animate="animate"
          >
            <div className="flex min-h-32 items-center justify-center">
              <div
                className={cn(
                    "group rounded-full border border-[#073E79] bg-[#ade8f4] text-base text-white transition-all ease-in hover:bg-[#b0e0f0] shadow-[0_0_10px_rgba(21,101,239,0.7)] hover:shadow-[0_0_20px_rgba(31,101,250,1)]"
                  )}
                >
                <ShinyTextBox className="inline-flex items-center justify-center px-4 py-1 transition ease-out hover:text-[#073E79] hover:duration-400">
                  <span>🚀 Waitlist Opening Soon</span>
                </ShinyTextBox>
              </div>
            </div>
          </motion.div>
          <motion.h1
            variants={fadeInUp(ANIMATION_DELAYS.HERO_TITLE)}
            initial="initial"
            animate="animate"
            className="text-6xl text-[#073E79] mb-4"
          >
            The{' '}
              <span className="relative text-[#073E79] font-bold inline-block z-10">
                Ultimate
                <Particles
                  className="absolute inset-0 z-[-10]"
                  quantity={100}
                  ease={80}
                  color="black"
                  refresh
                />
              </span>
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
