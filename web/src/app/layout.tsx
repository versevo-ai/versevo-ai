import './global.css';
import type { Metadata } from 'next';
import { Noto_Sans_Lao } from 'next/font/google';
import { type MetadataConfig } from '@/lib/types';
import { COMPANY_INFO } from '@/lib/constants';

const notoSansLao = Noto_Sans_Lao({
  subsets: ['latin'],
});

const metadataConfig: MetadataConfig = {
  title: COMPANY_INFO.NAME,
  description: COMPANY_INFO.TAGLINE,
  keywords: [
    'VersevoAI',
    'Audio AI',
    'AI Platform',
    'Audio Processing',
    'Machine Learning',
    'Translation',
    'Natural Language Processing',
    'Versveso',
    'Versevo.com',
    'Transcription',
    'Speech Recognition',
    'Transformer',
    'Audio Generation',
    'Voice Synthesis',
    'Expressive Text-to-Speech',
    'Expressive Translation',
    'Emotion Recognition',
    'AI Ethics',
    'AI Governance',
    'Open Source',
    'Security',
    'Alternative',
    'Versevo AI GitHub',
    'versevo.ai'
  ],
  ogImage: '/Logo.svg',
};

export const metadata: Metadata = {
  title: {
    default: metadataConfig.title,
    template: `%s | ${metadataConfig.title}`,
  },
  description: metadataConfig.description,
  keywords: metadataConfig.keywords,
  icons: {
    icon: './favicon.ico',
  },
  openGraph: {
    title: metadataConfig.title,
    description: metadataConfig.description,
    url: COMPANY_INFO.URL,
    type: 'website',
    locale: 'en_US',
    siteName: metadataConfig.title,
    images: [
      {
        url: metadataConfig.ogImage,
        width: 800,
        height: 600,
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: metadataConfig.title,
    description: metadataConfig.description,
    images: [metadataConfig.ogImage],
  },
  appleWebApp: {
    title: metadataConfig.title,
    statusBarStyle: 'default',
    capable: true,
    startupImage: metadataConfig.ogImage,
  },
};

interface RootLayoutProps {
  children: React.ReactNode;
}

const RootLayout: React.FC<RootLayoutProps> = ({ children }) => {
  return (
    <html lang="en">
      <body className={notoSansLao.className}>
        {children}
      </body>
    </html>
  );
};

export default RootLayout;
