"use client";
import {useState, useEffect} from "react"
import Header from "./header";
import JoinWaitlist from "./joinWaitlist";
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
        background: `radial-gradient(circle at ${mousePosition.x}% ${mousePosition.y}%, #00BFFF, #4169E1, #3CB371)`,
        transition: 'background 0.3s ease',
    }

    return (
        <div className="h-screen w-full flex flex-col overflow-hidden" style={gradientStyle}>
            <Header/>

            <div className="flex-grow flex items-center justify-center">
                <div className="max-w-3xl mx-auto py-16 px-4 text-center">  
                <h1 className="text-6xl font-bold text-white mb-4">
            The <span className="text-gray-200">Ultimate</span>
            <br />
            Audio AI Platform
          </h1>
          
          {/* Subheading */}
          <p className="text-white/80 mb-12 text-lg max-w-2xl mx-auto">
            Unlock Global Understanding. 200+ Languages. Seamless X-2-X Translation 
            & Transcription. We&apos;re breaking down language barriers, one breakthrough 
            at a time.
          </p>

          <div className="flex max-w-md mx-auto">
                <JoinWaitlist/>
            </div>
                </div>
                
            </div>

            
        </div>
    );
}