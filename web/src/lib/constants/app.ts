import { type TeamMember } from '@/lib/types';
import { SambitImg, ParthibImg, MaharshiImg, AriyanImg, AvikImg } from '@/public/team';

export const TEAM_MEMBERS: readonly TeamMember[] = [
  {
    name: 'Sambit Chakraborty',
    image: SambitImg,
    alt: 'Sambit Chakraborty',
    fallback: 'SG',
    gitHubProfile: 'Sambit003',
  },
  {
    name: 'Parthib Kumar Deb',
    image: ParthibImg,
    alt: 'Parthib Kumar Deb',
    fallback: 'PKD',
    gitHubProfile: 'PARTHIB-DEB',
  },
  {
    name: 'Maharshi Mahanti',
    image: MaharshiImg,
    alt: 'Maharshi Mahanti',
    fallback: 'MM',
    gitHubProfile: 'Esoteric-Coder',
  },
  {
    name: 'Ariyan Pandey',
    image: AriyanImg,
    alt: 'Ariyan Pandey',
    fallback: 'AP',
    gitHubProfile: 'Ariyanandey',
  },
  {
    name: 'Avik Mukherjee',
    image: AvikImg,
    alt: 'Avik Mukherjee',
    fallback: 'AM',
    gitHubProfile: 'Avik-creator',
  },
] as const;

export const AVATAR_SIZES = {
  sm: 'h-12 w-12',
  md: 'h-16 w-16',
  lg: 'h-20 w-20',
} as const;

export const ANIMATION_DELAYS = {
  HEADER: 0.2,
  HERO_TITLE: 0.2,
  HERO_DESCRIPTION: 0.4,
  HERO_TEAM_INFO: 0.4,
  HERO_AVATARS: 0.5,
  AVATAR_STAGGER: 0.1,
} as const;

export const COMPANY_INFO = {
  NAME: 'VersevoAI',
  TAGLINE: 'The Ultimate Audio AI Platform',
  DESCRIPTION: 'Unlock Global Understanding. 200+ Languages. Seamless Translation & Transcription. We\'re breaking down language barriers, one breakthrough at a time.',
  ORIGIN: 'Brought to you by, with ❤️ from India',
  URL: 'https://versevo.xyz',
} as const;
