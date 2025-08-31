'use client';

import React from 'react';
import { motion } from 'framer-motion';
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/Avatar';
import { type AvatarProps, type TeamMember } from '@/lib/types';
import { TEAM_MEMBERS, AVATAR_SIZES, ANIMATION_DELAYS } from '@/lib/constants';
import { scaleIn, staggerContainer } from '@/lib/utils/animations';
import { cn } from '@/src/lib/utils';

interface AvatarRowProps extends AvatarProps {
  members?: readonly TeamMember[];
}

export const AvatarRow: React.FC<AvatarRowProps> = ({
  members = TEAM_MEMBERS,
  size = 'md',
  className,
}) => {
  return (
    <motion.div
      variants={staggerContainer(ANIMATION_DELAYS.AVATAR_STAGGER)}
      initial="initial"
      animate="animate"
      className={cn('flex items-center gap-3', className)}
    >
      {members.map((member, index) => (
        <motion.div
          key={`${member.name}-${index}`}
          variants={scaleIn(index * ANIMATION_DELAYS.AVATAR_STAGGER)}
        >
          <Avatar
            className={cn(
              AVATAR_SIZES[size],
              'border-3 border-white shadow-xl ring-2 ring-blue-100/50',
              'hover:scale-105 transition-transform duration-200'
            )}
          >
            <AvatarImage
              src={member.image}
              alt={member.alt}
              className="object-cover object-center select-none"
            />
            <AvatarFallback className="bg-gradient-to-br from-blue-400 to-blue-600 text-white font-semibold text-sm">
              {member.fallback}
            </AvatarFallback>
          </Avatar>
        </motion.div>
      ))}
    </motion.div>
  );
};

export default AvatarRow;
