'use client';

import React from 'react';
import { motion } from 'framer-motion';
import { Avatar, AvatarFallback, AvatarImage } from '@/src/components/ui/shared/avatar';
import { type AvatarProps, type TeamMember } from '@/lib/types';
import { TEAM_MEMBERS, AVATAR_SIZES, ANIMATION_DELAYS } from '@/lib/constants';
import { scaleIn, staggerContainer } from '@/lib/utils/animations';
import { cn } from '@/src/lib/utils';
import { VirtualCursorCard } from '@/src/components/ui/shared/virtualCursorCard';
import { Card } from '@/src/components/ui/shared/Card';
import Image from 'next/image';

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
          <VirtualCursorCard
            placement="bottom-right"
            maxWidth={24}
            trigger={
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
            }
            overlay={
              <Card maxWidth={24} radius="l-4" direction="column" border="neutral-alpha-medium">
                <div className="flex flex-col p-4">
                  <div className="flex items-center gap-2">
                    <Avatar className={cn(AVATAR_SIZES['sm'])}>
                      <AvatarImage
                        src={member.image}
                        alt={member.alt}
                        className="object-cover object-center select-none"
                      />
                      <AvatarFallback className="bg-gradient-to-br from-blue-400 to-blue-600 text-white font-semibold text-sm">
                        {member.fallback}
                      </AvatarFallback>
                    </Avatar>
                    <div>
                      <p className="font-semibold">{member.name}</p>
                      <a
                        href={member.gitHubProfile}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-sm text-gray-500"
                      >
                        @{member.gitHubProfile.split('/').pop()}
                      </a>
                    </div>
                  </div>
                  <Image
                    src={`https://github.com/${member.gitHubProfile.split('/').pop()}.png`}
                    alt={`${member.name}'s GitHub profile picture`}
                    width={100}
                    height={100}
                    className="w-full h-auto mt-4 rounded-lg"
                  />
                  <p className="text-sm text-gray-600 mt-2">

                  </p>
                </div>
              </Card>
            }
          />
        </motion.div>
      ))}
    </motion.div>
  );
};

export default AvatarRow;
