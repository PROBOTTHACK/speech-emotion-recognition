import { motion } from "framer-motion";

const BackgroundEffects = () => {
  return (
    <div className="fixed inset-0 overflow-hidden -z-10">

      {/* TOP CYAN GLOW */}
      <motion.div
        animate={{
          x: [0, 40, 0],
          y: [0, -30, 0],
        }}
        transition={{
          duration: 10,
          repeat: Infinity,
          ease: "easeInOut",
        }}
        className="absolute top-[-120px] left-[-100px] w-[350px] h-[350px] bg-cyan-500/20 rounded-full blur-[120px]"
      />

      {/* PURPLE CENTER GLOW */}
      <motion.div
        animate={{
          x: [0, -50, 0],
          y: [0, 50, 0],
        }}
        transition={{
          duration: 14,
          repeat: Infinity,
          ease: "easeInOut",
        }}
        className="absolute top-[20%] right-[10%] w-[400px] h-[400px] bg-purple-500/20 rounded-full blur-[140px]"
      />

      {/* BOTTOM BLUE GLOW */}
      <motion.div
        animate={{
          x: [0, 30, 0],
          y: [0, 40, 0],
        }}
        transition={{
          duration: 12,
          repeat: Infinity,
          ease: "easeInOut",
        }}
        className="absolute bottom-[-120px] left-[20%] w-[300px] h-[300px] bg-blue-500/20 rounded-full blur-[120px]"
      />

      {/* GRID OVERLAY */}
      <div
        className="absolute inset-0 opacity-[0.03]"
        style={{
          backgroundImage:
            "linear-gradient(rgba(255,255,255,0.1) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.1) 1px, transparent 1px)",
          backgroundSize: "60px 60px",
        }}
      />

    </div>
  );
};

export default BackgroundEffects;