import { motion } from "framer-motion";

const Loader = () => {
  return (
    <div className="flex flex-col items-center justify-center mt-10">

      <motion.div
        animate={{
          rotate: 360,
        }}
        transition={{
          repeat: Infinity,
          duration: 1,
          ease: "linear",
        }}
        className="w-16 h-16 border-4 border-cyan-400 border-t-transparent rounded-full"
      />

      <p className="mt-6 text-cyan-400 text-lg">
        Analyzing emotional patterns...
      </p>
    </div>
  );
};

export default Loader;