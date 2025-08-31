import { Avatar, AvatarFallback, AvatarImage } from "@components/ui/avatar";
import { motion } from "framer-motion";
import { SambitImg, ParthibImg, MaharshiImg, AriyanImg, AvikImg } from "@public/team";

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
      src: SambitImg,
      alt: "Sambit Chakraborty",
      fallback: "SG",
    },
    {
      src: ParthibImg,
      alt: "Parthib Kumar Deb",
      fallback: "PKD",
    },
    {
      src: MaharshiImg,
      alt: "Maharshi Mahanti",
      fallback: "MM",
    },
    {
      src: AriyanImg,
      alt: "Ariyan Pandey",
      fallback: "AP",
    },
        {
      src: AvikImg,
      alt: "Avik Mukherjee",
      fallback: "AM",
    }
  ];

  const avatarsToShow =
    avatars && avatars.length > 0 ? avatars : defaultAvatars;

  return (
    <div className={`flex items-center gap-3 ${className}`}>
      {[...avatarsToShow].map((avatar, index) => (
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
              className="object-cover object-center select-none"
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
