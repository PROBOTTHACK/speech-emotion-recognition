import { motion } from "framer-motion";

import {
  Mic,
  Square,
  Sparkles,
  AudioLines,
} from "lucide-react";

import toast from "react-hot-toast";

import API from "../services/api";

import useRecorder from "../hooks/useRecorder";
import { useState } from "react";

import EmotionCard from "./EmotionCard";
import EmotionChart from "./EmotionChart";

const AudioRecorder = () => {
    const [prediction, setPrediction] = useState(null);

  const {
    isRecording,
    audioURL,
    audioBlob,
    startRecording,
    stopRecording,
  } = useRecorder();

  const handlePrediction = async () => {

    if (!audioBlob) {
      toast.error("Please record audio first.");
      return;
    }

    try {

      toast.loading("Analyzing voice emotion...", {
        id: "prediction",
      });

      const formData = new FormData();

      formData.append(
        "file",
        audioBlob,
        "recording.wav"
      );

      const response = await API.post(
        "/predict",
        formData,
        {
          headers: {
            "Content-Type":
              "multipart/form-data",
          },
        }
      );

      toast.success(
        `Detected Emotion: ${response.data.emotion}`,
        {
          id: "prediction",
        }
      );

      setPrediction(response.data);

    console.log(response.data);

    } catch (error) {

      console.error(error);

      toast.error(
        "Prediction failed.",
        {
          id: "prediction",
        }
      );
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 30 }}
      animate={{ opacity: 1, y: 0 }}
      className="mt-14 backdrop-blur-xl bg-white/5 border border-white/10 rounded-3xl p-8 shadow-[0_0_40px_rgba(139,92,246,0.08)]"
    >

      {/* HEADER */}
      <div className="text-center mb-10">

        <div className="flex items-center justify-center gap-2 mb-4">
          <Sparkles className="text-purple-400" />

          <p className="uppercase tracking-[0.3em] text-sm text-purple-400">
            Realtime Voice AI
          </p>
        </div>

        <h2 className="text-4xl font-bold">
          Live Emotion Recording
        </h2>

        <p className="text-gray-400 mt-4">
          Record your voice directly and let AI
          analyze emotional patterns in realtime.
        </p>
      </div>

      {/* RECORD BUTTON */}
      <div className="flex justify-center">

        {!isRecording ? (

          <motion.button
            whileHover={{
              scale: 1.08,
              boxShadow:
                "0px 0px 35px rgba(168,85,247,0.45)",
            }}
            whileTap={{ scale: 0.95 }}
            onClick={startRecording}
            className="w-24 h-24 rounded-full bg-gradient-to-r from-purple-500 to-cyan-500 flex items-center justify-center shadow-2xl"
          >
            <Mic className="w-10 h-10 text-white" />
          </motion.button>

        ) : (

          <motion.button
            animate={{
              scale: [1, 1.1, 1],
            }}
            transition={{
              repeat: Infinity,
              duration: 1,
            }}
            whileTap={{ scale: 0.95 }}
            onClick={stopRecording}
            className="w-24 h-24 rounded-full bg-red-500 flex items-center justify-center shadow-2xl shadow-red-500/40"
          >
            <Square className="w-10 h-10 text-white" />
          </motion.button>

        )}
      </div>

      {/* RECORDING STATUS */}
      <div className="text-center mt-6">

        {isRecording ? (

          <motion.p
            animate={{
              opacity: [0.5, 1, 0.5],
            }}
            transition={{
              repeat: Infinity,
              duration: 1.2,
            }}
            className="text-red-400 font-medium"
          >
            ● Recording in progress...
          </motion.p>

        ) : (

          <p className="text-gray-400">
            Click the microphone to start recording
          </p>

        )}
      </div>

      {/* AUDIO PLAYER */}
      {audioURL && (

        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="mt-10"
        >

          <div className="flex items-center gap-2 mb-4">
            <AudioLines className="text-cyan-400" />

            <p className="text-cyan-400 font-medium">
              Recorded Audio Preview
            </p>
          </div>

          <audio
            controls
            src={audioURL}
            className="w-full opacity-80 hover:opacity-100 transition-all"
          />

          {/* PREDICT BUTTON */}
          <motion.button
            whileHover={{
              scale: 1.02,
              boxShadow:
                "0px 0px 30px rgba(34,211,238,0.35)",
            }}
            whileTap={{ scale: 0.98 }}
            onClick={handlePrediction}
            className="w-full mt-8 py-4 rounded-2xl bg-gradient-to-r from-cyan-500 to-purple-600 text-white font-semibold text-lg shadow-xl"
          >
            Predict Recorded Emotion
          </motion.button>

        </motion.div>
      )}
      {prediction && (
        <>
            <EmotionCard
            emotion={prediction.emotion}
            confidence={prediction.confidence}
            />

            <EmotionChart
            probabilities={prediction.probabilities}
            />
        </>
        )}

    </motion.div>
  );
};

export default AudioRecorder;
