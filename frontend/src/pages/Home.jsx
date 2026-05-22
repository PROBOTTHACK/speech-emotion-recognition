import Navbar from "../components/Navbar";
import AudioUpload from "../components/AudioUpload";

const Home = () => {
  return (
    <div className="min-h-screen bg-[#0B0F19] text-white overflow-hidden">
      <Navbar />

      <div className="px-6">
        <AudioUpload />
      </div>
    </div>
  );
};

export default Home;