import type { Metadata } from "next";
import "./globals.css";
import {Noto_Sans_Lao} from "next/font/google";

const notoSansLao = Noto_Sans_Lao({
  subsets: ["latin"],
})


export const metadata: Metadata = {
  title: {
    default: "VersevoAI",
    template: "%s | VersevoAI",
  },
  description: "The Ultimate Audio AI Platform",
  keywords: ["VersevoAI", "Audio AI", "AI Platform", "Audio Processing", "Machine Learning", "Translation"],
  icons:{
    icon: "/Logo.svg",
  },

  openGraph:{
    title: "VersevoAI",
    description: "The Ultimate Audio AI Platform",
    url: "https://versevo.ai",
    type: "website",
    locale: "en_US",
    siteName: "VersevoAI",
    images: [
      {
        url: "/Logo.svg",
        width: 800,
        height: 600,
      },
    ],
  },

  twitter: {
    card: "summary_large_image",
    title: "VersevoAI",
    description: "The Ultimate Audio AI Platform",
    images: ["/Logo.svg"],
  },
  appleWebApp: {
    title: "VersevoAI",
    statusBarStyle: "default",
    capable: true,
    startupImage: "/Logo.svg",
  }
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={notoSansLao.className}>
        {children}
      </body>
    </html>
  );
}
