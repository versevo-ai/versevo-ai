"use client";

import Header from "@components/ui/navbar";
import { motion } from "framer-motion";
import Image from "next/image";
import { ConversationImg } from "@public/hero";
import { AvatarRow } from "@components/ui/landing/avatarRow";

export default function Hero() {
  return (
    <div className="h-screen overflow-y-auto w-full flex flex-col bg-gradient-to-br from-blue-500 via-blue-300 to-cyan-200">
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="flex items-center justify-center"
      >
        <Header />
      </motion.div>

      <div className="flex-grow flex items-center justify-center">
        <div className="max-w-3xl mx-auto py-16 px-4 text-center">
          <motion.h1
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.2 }}
            className="text-6xl text-[#073E79] mb-4"
          >
            The <span className="text-[#073E79] font-bold">Ultimate</span>
            <br />
            Audio AI Platform
          </motion.h1>

          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.4 }}
            className="text-[#073E79] mb-12 font-normal max-w-2xl mx-auto"
          >
            Unlock Global Understanding. 200+ Languages. Seamless Translation &
            Transcription. We&apos;re breaking down language barriers, one
            breakthrough at a time.
          </motion.p>

          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.4 }}
            className="text-[#073E79] mb-6 font-semibold max-w-2xl mx-auto"
          >
            Brought to you by, with ❤️ from India
          </motion.p>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.5 }}
            className="mb-12 flex justify-center"
          >
            <AvatarRow size="sm" className="" />
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.6 }}
            className="flex-grow flex items-center justify-center max-w-md mx-auto my-auto"
          >
          </motion.div>
        </div>
      </div>
    </div>
  );
}
