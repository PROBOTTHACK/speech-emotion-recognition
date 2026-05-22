import { motion } from "framer-motion";
import { BrainCircuit, AudioWaveform } from "lucide-react";

const Navbar = () => {
  return (
    <motion.nav
      initial={{ y: -40, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.6 }}
      className="w-full fixed top-0 left-0 z-50 px-6 py-4"
    >
      <div className="max-w-7xl mx-auto">
        <div className="backdrop-blur-xl bg-white/5 border border-white/10 rounded-2xl px-6 py-4 shadow-2xl">
          
          <div className="flex items-center justify-between">
            
            {/* LEFT SIDE */}
            <div className="flex items-center gap-3">
              
              <div className="p-3 rounded-xl bg-gradient-to-br from-cyan-500 to-purple-600 shadow-lg shadow-cyan-500/20">
                <BrainCircuit className="text-white w-6 h-6" />
              </div>

              <div>
                <h1 className="text-xl font-bold tracking-wide bg-gradient-to-r from-cyan-400 to-purple-500 bg-clip-text text-transparent">
                  SER AI
                </h1>

                <p className="text-xs text-gray-400 tracking-wider">
                  Speech Emotion Intelligence
                </p>
              </div>
            </div>

            {/* CENTER NAV */}
            <div className="hidden md:flex items-center gap-8">
              
              <button className="text-gray-300 hover:text-cyan-400 transition-all duration-300 text-sm font-medium">
                Dashboard
              </button>

              <button className="text-gray-300 hover:text-cyan-400 transition-all duration-300 text-sm font-medium">
                Analytics
              </button>

              <button className="text-gray-300 hover:text-cyan-400 transition-all duration-300 text-sm font-medium">
                Realtime AI
              </button>

            </div>

            {/* RIGHT SIDE */}
            <div className="flex items-center gap-4">

              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="hidden md:flex items-center gap-2 px-4 py-2 rounded-xl bg-white/5 border border-white/10 hover:border-cyan-400/40 transition-all duration-300 text-sm text-gray-300"
              >
                {/* <GithubIcon size={18} /> */}
                GitHub
              </motion.button>

              <motion.button
                whileHover={{
                  scale: 1.05,
                  boxShadow: "0px 0px 25px rgba(34,211,238,0.4)",
                }}
                whileTap={{ scale: 0.95 }}
                className="flex items-center gap-2 px-5 py-2.5 rounded-xl bg-gradient-to-r from-cyan-500 to-purple-600 text-white font-semibold shadow-lg"
              >
                <AudioWaveform size={18} />
                Predict
              </motion.button>

            </div>
          </div>
        </div>
      </div>
    </motion.nav>
  );
};

export default Navbar;