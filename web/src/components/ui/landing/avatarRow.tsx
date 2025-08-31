import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { motion } from "framer-motion";

interface AvatarRowProps {
  avatars?: Array<{
    src?: string;
    alt: string;
    fallback: string;
  }>;
  size?: "sm" | "md" | "lg";
  className?: string;
}

export function AvatarRow({
  avatars,
  size = "md",
  className = "",
}: AvatarRowProps) {
  const sizeClasses = {
    sm: "h-12 w-12",
    md: "h-16 w-16",
    lg: "h-20 w-20",
  };

  const defaultAvatars = [
    {
      src: "/images/pic-1.jpg",
      alt: "Avik Mukherjee",
      fallback: "AM",
    },
    {
      src: "/images/pic-2.jpg",
      alt: "Sambit Ghosh",
      fallback: "SG",
    },
    {
      src: "/images/pic-3.jpg",
      alt: "Parthib Kumar Deb",
      fallback: "PKD",
    },
    {
      src: "/images/pic-4.jpg",
      alt: "User 4",
      fallback: "U4",
    },
    {
      src: "/images/pic-5.png",
      alt: "User 5",
      fallback: "U5",
    },
  ];

  const avatarsToShow =
    avatars && avatars.length > 0 ? avatars : defaultAvatars;

  return (
    <div className={`flex items-center gap-3 ${className}`}>
      {[...avatarsToShow].reverse().map((avatar, index) => (
        <motion.div
          key={index}
          initial={{ opacity: 0, scale: 0.8, y: 10 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          transition={{
            duration: 0.3,
            delay: index * 0.1,
            ease: "easeOut"
          }}
        >
          <Avatar
            className={`${sizeClasses[size]} border-3 border-white shadow-xl ring-2 ring-blue-100/50 hover:scale-105 transition-transform duration-200`}
          >
            <AvatarImage
              src={avatar.src || "/placeholder.svg"}
              alt={avatar.alt}
              className="object-cover object-center"
            />
            <AvatarFallback className="bg-gradient-to-br from-blue-400 to-blue-600 text-white font-semibold text-sm">
              {avatar.fallback}
            </AvatarFallback>
          </Avatar>
        </motion.div>
      ))}
    </div>
  );
}
