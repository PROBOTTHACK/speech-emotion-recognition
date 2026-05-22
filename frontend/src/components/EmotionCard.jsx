import { motion } from "framer-motion";
import { Brain } from "lucide-react";

const EmotionCard = ({ emotion, confidence }) => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 30 }}
      animate={{ opacity: 1, y: 0 }}
      className="mt-10 backdrop-blur-xl bg-white/5 border border-white/10 rounded-3xl p-8 shadow-[0_0_30px_rgba(139,92,246,0.15)]"
    >
      <div className="flex items-center gap-3 mb-6">
        <Brain className="text-cyan-400" />
        
        <h2 className="text-2xl font-semibold">
          Prediction Result
        </h2>
      </div>

      <div className="space-y-5">

        <div>
          <p className="text-gray-400 text-sm mb-2">
            Detected Emotion
          </p>

          <h1 className="text-5xl font-bold bg-gradient-to-r from-cyan-400 to-purple-500 bg-clip-text text-transparent capitalize">
            {emotion}
          </h1>
        </div>

        <div>
          <p className="text-gray-400 text-sm mb-2">
            Confidence Score
          </p>

          <div className="w-full bg-white/10 rounded-full h-4 overflow-hidden">
            <motion.div
              initial={{ width: 0 }}
              animate={{ width: `${confidence}%` }}
              transition={{ duration: 1 }}
              className="h-full bg-gradient-to-r from-cyan-400 to-purple-500"
            />
          </div>

          <p className="mt-2 text-cyan-400 font-semibold">
            {confidence.toFixed(2)}%
          </p>
        </div>
      </div>
    </motion.div>
  );
};

export default EmotionCard;