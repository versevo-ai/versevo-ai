"use client";
import {useState, useEffect} from "react"
import Header from "./header";
import JoinWaitlist from "./joinWaitlist";
import { motion } from "framer-motion"; 

export default function Hero() {
    const [mousePosition, setMousePosition] = useState({ x: 0, y: 0 });

    useEffect(() => {
        const handleMouseMove = (e: MouseEvent) => {
            const x = (e.clientX / window.innerWidth) * 100;
            const y = (e.clientY / window.innerHeight) * 100;
            setMousePosition({ x, y });
        };

        window.addEventListener('mousemove', handleMouseMove);
    
        return () => {
            window.removeEventListener('mousemove', handleMouseMove);
        };
    }, []);

    const gradientStyle = {
        width: '100vw',
        height: '100vh',
        background: `
          radial-gradient(circle at ${mousePosition.x}% ${mousePosition.y}%, rgba(60, 179, 113, 0.6) 0%, transparent 20%),
          #00BFFF
        `,
        backgroundBlendMode: 'screen',
        transition: 'background 0.1s ease-out',
      };
      

    return (
        <div className="h-screen w-full flex flex-col overflow-hidden" style={gradientStyle}>
            <motion.div 
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5 }}
                className="flex items-center justify-center"
            >
                <Header/>
            </motion.div>

            <div className="flex-grow flex items-center justify-center">
                <div className="max-w-3xl mx-auto py-8 md:py-16 px-4 text-center">  
                    <motion.h1 
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.5, delay: 0.2 }}
                        className="text-4xl md:text-5xl lg:text-6xl font-bold text-white mb-3 md:mb-4"
                    >
                        The <span className="text-gray-200">Ultimate</span>
                        <br />
                        Audio AI Platform
                    </motion.h1>
          
                    <motion.p 
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.5, delay: 0.4 }}
                        className="text-white/80 mb-8 md:mb-12 text-base md:text-lg max-w-2xl mx-auto px-2"
                    >
                        Unlock Global Understanding. 200+ Languages. Seamless X-2-X Translation 
                        & Transcription. We&apos;re breaking down language barriers, one breakthrough 
                        at a time.
                    </motion.p>

                    <motion.div 
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.5, delay: 0.6 }}
                        className="flex-grow flex items-center justify-center max-w-xs sm:max-w-sm md:max-w-md mx-auto my-auto"
                    >
                        <JoinWaitlist/>
                    </motion.div>
                </div>
            </div>
        </div>
    );
}