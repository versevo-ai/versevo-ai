"use client";

import Header from "./header";
import JoinWaitlist from "./joinWaitlist";
import { motion } from "framer-motion";
import Image from "next/image";
import imageConversation from "@/../public/imageConversation.png";
import { AvatarRow } from "./landing/avatarRow";

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
            <JoinWaitlist />
          </motion.div>
        </div>
      </div>
      <div className="w-full pb-16 mt-16">
        <div className="grid md:grid-cols-2 gap-6 items-center justify-around">
          <motion.div
            initial={{ opacity: 0, x: -50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.7, delay: 0.8 }}
            className="flex justify-center"
          >
            <div className="rounded-2xl overflow-hidden shadow-2xl max-w-lg">
              <Image
                src={imageConversation}
                alt="Business conversation illustration"
                width={900}
                height={600}
                className="w-full h-auto object-cover"
              />
            </div>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, x: 50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.7, delay: 1.0 }}
            className="text-center items-center justify-center"
          >
            <h2 className="text-3xl md:text-4xl text-[#073E79] mb-6">
              Keep <span className="font-extrabold">Confidence</span>
              <br />
              in your{" "}
              <span className="font-extrabold">
                Mother
                <br />
                Language
              </span>
            </h2>
            <p className="text-[#073E79] text-lg leading-relaxed opacity-90">
              Unlock the best version of you in{" "}
              <span className="font-semibold">Business Deals</span>
              <br />
              while we handle the translation, with best ever
              <br />
              accuracy
            </p>
          </motion.div>
        </div>
      </div>
    </div>
  );
}
