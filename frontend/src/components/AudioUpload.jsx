import { useCallback, useState } from "react";
import { useDropzone } from "react-dropzone";
import { motion } from "framer-motion";
import { UploadCloud, FileAudio, Sparkles } from "lucide-react";

const AudioUpload = () => {
  const [file, setFile] = useState(null);

  const onDrop = useCallback((acceptedFiles) => {
    if (acceptedFiles.length > 0) {
      setFile(acceptedFiles[0]);
    }
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      "audio/wav": [".wav"],
    },
    multiple: false,
  });

  return (
    <motion.div
      initial={{ opacity: 0, y: 40 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6 }}
      className="w-full max-w-3xl mx-auto mt-32"
    >
      <div className="backdrop-blur-xl bg-white/5 border border-white/10 rounded-3xl p-8 shadow-[0_0_40px_rgba(0,255,255,0.08)]">

        {/* TOP TEXT */}
        <div className="text-center mb-8">
          
          <div className="flex items-center justify-center gap-2 mb-4">
            <Sparkles className="text-cyan-400" />
            <p className="text-cyan-400 uppercase tracking-[0.3em] text-sm">
              AI Emotion Detection
            </p>
          </div>

          <h2 className="text-4xl font-bold text-white">
            Upload Voice Sample
          </h2>

          <p className="text-gray-400 mt-4">
            Drag and drop your WAV audio file for AI-powered
            speech emotion analysis.
          </p>
        </div>

        {/* DROPZONE */}
        <motion.div
          whileHover={{ scale: 1.01 }}
          {...getRootProps()}
          className={`border-2 border-dashed rounded-3xl p-14 text-center cursor-pointer transition-all duration-300
          
          ${
            isDragActive
              ? "border-cyan-400 bg-cyan-400/10"
              : "border-white/10 hover:border-cyan-400/40 hover:bg-white/5"
          }`}
        >
          <input {...getInputProps()} />

          <div className="flex flex-col items-center">

            <div className="p-5 rounded-full bg-gradient-to-br from-cyan-500/20 to-purple-500/20 mb-6">
              <UploadCloud className="w-14 h-14 text-cyan-400" />
            </div>

            {file ? (
              <>
                <div className="flex items-center gap-3 bg-white/5 px-5 py-3 rounded-2xl border border-white/10">
                  <FileAudio className="text-purple-400" />
                  
                  <span className="text-gray-200 font-medium">
                    {file.name}
                  </span>
                </div>

                <p className="text-sm text-green-400 mt-4">
                  File ready for prediction
                </p>
              </>
            ) : (
              <>
                <p className="text-xl text-gray-200 font-semibold">
                  Drag & Drop WAV File
                </p>

                <p className="text-gray-500 mt-3">
                  or click to browse from your device
                </p>
              </>
            )}
          </div>
        </motion.div>

        {/* BUTTON */}
        <motion.button
          whileHover={{
            scale: 1.03,
            boxShadow: "0px 0px 30px rgba(34,211,238,0.35)",
          }}
          whileTap={{ scale: 0.97 }}
          className="w-full mt-8 py-4 rounded-2xl bg-gradient-to-r from-cyan-500 to-purple-600 text-white font-semibold text-lg shadow-xl"
        >
          Predict Emotion
        </motion.button>
      </div>
    </motion.div>
  );
};

export default AudioUpload;