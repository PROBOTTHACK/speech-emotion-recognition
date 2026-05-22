import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./style.css";

import { Toaster } from "react-hot-toast";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <>
      <Toaster
        position="top-right"
        toastOptions={{
          duration: 3000,
          style: {
            background: "rgba(15,23,42,0.95)",
            color: "#fff",
            border: "1px solid rgba(255,255,255,0.08)",
            backdropFilter: "blur(10px)",
            padding: "14px 18px",
            borderRadius: "16px",
          },
        }}
      />

      <App />
    </>
  </React.StrictMode>
);