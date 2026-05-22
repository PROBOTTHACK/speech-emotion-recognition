import { useRef, useState } from "react";

const useRecorder = () => {

  const [isRecording, setIsRecording] = useState(false);

  const [audioURL, setAudioURL] = useState(null);

  const [audioBlob, setAudioBlob] = useState(null);

  const mediaRecorderRef = useRef(null);

  const audioChunksRef = useRef([]);

  const startRecording = async () => {

    try {

      const stream =
        await navigator.mediaDevices.getUserMedia({
          audio: true,
        });

      const mediaRecorder =
        new MediaRecorder(stream);

      mediaRecorderRef.current = mediaRecorder;

      audioChunksRef.current = [];

      mediaRecorder.ondataavailable = (event) => {

        if (event.data.size > 0) {
          audioChunksRef.current.push(event.data);
        }
      };

      mediaRecorder.onstop = () => {

        const blob = new Blob(
          audioChunksRef.current,
          {
            type: "audio/wav",
          }
        );

        const url = URL.createObjectURL(blob);

        setAudioBlob(blob);

        setAudioURL(url);
      };

      mediaRecorder.start();

      setIsRecording(true);

    } catch (error) {

      console.error("Microphone access denied:", error);
    }
  };

  const stopRecording = () => {

    if (mediaRecorderRef.current) {

      mediaRecorderRef.current.stop();

      setIsRecording(false);
    }
  };

  return {
    isRecording,
    audioURL,
    audioBlob,
    startRecording,
    stopRecording,
  };
};

export default useRecorder;