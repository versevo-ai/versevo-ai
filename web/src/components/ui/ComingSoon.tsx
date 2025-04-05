"use client";
import { motion } from "framer-motion";
import {Clock} from "lucide-react"

export default function ComingSoon() {
  return (
    <motion.div 
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, delay: 0.8 }}
      className="w-full py-4 md:py-6 text-center absolute bottom-0 left-0 backdrop-blur-sm bg-white/10"
    >
      <div className="container mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-4">
        <div className="flex items-center">
          <Clock size={20} className="text-white/60 mr-2" />
          <p className="text-white font-medium text-sm md:text-base">
            Launching Summer 2025
          </p>
        </div>
        
       
      </div>
      
      <div className="container mx-auto mt-3 md:mt-4 px-4">
        <div className="w-full bg-white/20 h-1 rounded-full overflow-hidden">
          <motion.div 
            initial={{ width: "0%" }}
            animate={{ width: "35%" }}
            transition={{ duration: 2, delay: 1 }}
            className="h-full bg-white rounded-full"
          />
        </div>
        <p className="text-white/60 text-xs mt-1 md:mt-2">Development Progress: 35%</p>
      </div>
    </motion.div>
  );
}