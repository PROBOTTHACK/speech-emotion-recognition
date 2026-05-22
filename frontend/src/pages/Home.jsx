import Navbar from "../components/Navbar";
import AudioUpload from "../components/AudioUpload";
import BackgroundEffects from "../components/BackgroundEffects";
import AudioRecorder from "../components/AudioRecorder";

const Home = () => {
  return (
    <div className="min-h-screen bg-[#0B0F19] text-white overflow-hidden relative">

      <BackgroundEffects />

      <Navbar />

      <div className="px-6 relative z-10">
        <AudioUpload />
        <AudioRecorder />
      </div>

    </div>
  );
};

export default Home;