<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=26&pause=1000&color=A78BFA&center=true&vCenter=true&width=700&lines=Speech+Emotion+Recognition;CNN+%2B+LSTM+%7C+FastAPI+%7C+React;Detecting+emotions+from+raw+audio" alt="Typing SVG" />

<br/>

> **Deep learning system that classifies human emotions from raw audio using a CNN + LSTM architecture — served via FastAPI and visualized through a React frontend.**

<br/>

![Status](https://img.shields.io/badge/Status-In_Development-fbbf24?style=for-the-badge&logo=github&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-a78bfa?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-fbbf24?style=for-the-badge&logo=tensorflow&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-2dd4bf?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-Frontend-60a5fa?style=for-the-badge&logo=react&logoColor=white)

</div>

---

## 🧠 What Is This?

**Speech Emotion Recognition (SER)** is the task of automatically identifying a speaker's emotional state from their voice. This project builds a full-stack SER system:

- **Model**: A CNN extracts spatial features from Mel spectrograms; an LSTM captures temporal patterns across time — together they classify 8 core emotions from audio input.
- **Backend**: A FastAPI server loads the trained model and exposes a REST inference endpoint.
- **Frontend**: A React interface lets users upload audio and receive real-time emotion predictions.

This is a complete **AI engineering project** — not just a Jupyter notebook. It covers the full pipeline from raw audio to a deployed, callable API with a production-style frontend.

---

## 🎯 Emotions Detected

| Label | Emotion | Label | Emotion |
|-------|---------|-------|---------|
| 01 | Neutral | 05 | Angry |
| 02 | Calm | 06 | Fearful |
| 03 | Happy | 07 | Disgusted |
| 04 | Sad | 08 | Surprised |

> Emotion labels follow the RAVDESS annotation standard.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────┐
│                  Audio Input                 │
│           (.wav / .mp3 / mic feed)           │
└────────────────────┬────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────┐
│           Preprocessing Pipeline            │
│  • Resample to 22050 Hz                     │
│  • Trim silence (librosa)                   │
│  • Extract Mel Spectrogram (128 mel bands)  │
│  • Normalize & pad to fixed length          │
└────────────────────┬────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────┐
│              CNN Feature Extractor           │
│  Conv2D → BatchNorm → ReLU → MaxPool (×3)   │
│  Captures local frequency-time patterns     │
└────────────────────┬────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────┐
│            LSTM Sequence Modeler             │
│  Bidirectional LSTM (×2) + Dropout          │
│  Captures temporal dependencies in speech   │
└────────────────────┬────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────┐
│              Dense Output Layer              │
│  FC(256) → Dropout → Softmax(8 classes)     │
└────────────────────┬────────────────────────┘
                     │
                     ▼
              Emotion Prediction
```

---

## 📦 Datasets

Training uses a combination of four benchmark SER datasets for robust generalization:

| Dataset | Speakers | Samples | Languages | Emotions |
|---------|----------|---------|-----------|----------|
| [RAVDESS](https://zenodo.org/record/1188976) | 24 | 2,452 | English | 8 |
| [TESS](https://tspace.library.utoronto.ca/handle/1807/24487) | 2 | 2,800 | English | 7 |
| [CREMA-D](https://github.com/CheyneyComputerScience/CREMA-D) | 91 | 7,442 | English | 6 |
| [SAVEE](http://kahlan.eps.surrey.ac.uk/savee/) | 4 | 480 | English | 7 |

> **Initial training starts with RAVDESS.** TESS, CREMA-D, and SAVEE are added progressively to improve generalization across accents, ages, and recording conditions.

---

## 🔬 Why CNN + LSTM?

This architecture is a deliberate design choice, not arbitrary:

- **CNNs** treat the Mel spectrogram as a 2D image — they learn local patterns like pitch shifts, voiced/unvoiced transitions, and formant structures that are spatially localized in frequency-time space.
- **LSTMs** process the sequence of CNN-extracted features across time — they capture the *temporal evolution* of emotion, which is crucial since emotions unfold over hundreds of milliseconds, not instantaneously.
- **Together**: CNN handles *what* features exist at each moment; LSTM handles *how* those features evolve — making this architecture well-suited for audio emotion tasks.

---

## 🗂️ Project Structure

```
speech-emotion-recognition/
│
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app entry point
│   │   ├── routes/
│   │   │   └── predict.py       # /predict endpoint
│   │   ├── model/
│   │   │   ├── ser_model.h5     # Trained Keras model
│   │   │   └── loader.py        # Model loading + caching
│   │   └── utils/
│   │       └── audio.py         # Preprocessing pipeline
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── AudioUploader.jsx
│   │   │   ├── EmotionResult.jsx
│   │   │   └── ConfidenceBar.jsx
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
├── notebooks/
│   ├── 01_eda.ipynb             # Dataset exploration
│   ├── 02_preprocessing.ipynb  # Feature engineering
│   └── 03_training.ipynb       # Model training & evaluation
│
├── data/
│   └── raw/                    # Dataset files (gitignored)
│
├── README.md
└── .gitignore
```

---

## ⚙️ Local Setup

### Prerequisites
- Python 3.10+
- Node.js 18+
- `ffmpeg` installed (required by librosa for audio decoding)

---

### Backend

```bash
cd backend
python -m venv env
source env/bin/activate        # Windows: env\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend runs at `http://127.0.0.1:8000`

API docs (auto-generated by FastAPI): `http://127.0.0.1:8000/docs`

**Key endpoint:**

```http
POST /predict
Content-Type: multipart/form-data

file: <audio file (.wav / .mp3)>

Response:
{
  "emotion": "happy",
  "confidence": 0.87,
  "all_scores": { "neutral": 0.04, "happy": 0.87, "sad": 0.02, ... }
}
```

---

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at `http://localhost:5173`

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Model** | TensorFlow / Keras | CNN + LSTM architecture |
| **Audio** | librosa | Mel spectrogram extraction, preprocessing |
| **Backend** | FastAPI | REST inference API |
| **Server** | Uvicorn | ASGI server |
| **Frontend** | React + Vite | UI — audio upload & results |
| **Notebooks** | Jupyter | EDA, training, evaluation |
| **Language** | Python 3.10+ / JavaScript | Core + UI |

---

## 🗺️ Roadmap

- [x] Architecture designed (CNN + LSTM)
- [x] Dataset pipeline (RAVDESS → TESS → CREMA-D → SAVEE)
- [x] FastAPI backend skeleton
- [x] React frontend skeleton
- [ ] Model training complete — RAVDESS baseline
- [ ] Multi-dataset training + evaluation
- [ ] Real-time microphone input (WebRTC)
- [ ] WebSocket streaming for live predictions
- [ ] Emotion confidence visualization (bar chart)
- [ ] Analytics dashboard (emotion history)
- [ ] Transformer-based upgrade (Wav2Vec2 / HuBERT)
- [ ] Docker deployment

---

## 📚 Key Concepts Demonstrated

This project is a practical implementation across several domains:

```
Audio Signal Processing   →   Mel spectrograms, MFCC, sampling theory
Deep Learning             →   CNN feature extraction, LSTM sequence modeling
Model Serving             →   FastAPI, REST API design, async inference
Full Stack AI             →   End-to-end: data → model → API → UI
Software Engineering      →   Modular structure, separation of concerns
```

---

## 🤝 Contributing

This is an active learning project. Issues, suggestions, and PRs are welcome.

---

<div align="center">

*Part of an ongoing AI engineering portfolio — building real systems, not just notebooks.*


</div>
