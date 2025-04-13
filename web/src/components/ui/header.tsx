import Logo from "@/../public/Logo.svg";
import Image from "next/image";
import { motion } from "framer-motion";

export default function Header() {
    return (
        <motion.div 
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
            className="flex items-center gap-x-2 bg-[#B2E2F0] rounded-[20px] px-4 sm:px-6 py-2 sm:py-3 shadow-md mt-4 sm:mt-8 w-[90%] sm:w-4/5 mx-auto"
        >
            <motion.div
                whileHover={{ scale: 1.1 }}
                whileTap={{ scale: 0.9 }}
            >
                <Image
                    src={Logo}
                    alt="Versevo Logo"
                    width={24}
                    height={28}
                    className="sm:w-[28px] sm:h-[32px]"
                />
            </motion.div>

            <motion.h1 
                className="text-xl sm:text-2xl font-semibold text-blue-900"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 0.2, duration: 0.5 }}
            >
                Versevo<span className="font-bold">AI</span>
            </motion.h1>
        </motion.div>
    );
}
