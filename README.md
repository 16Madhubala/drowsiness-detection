# Drowsiness Detection 🚗😴

**Real-time drowsiness detection using OpenCV & MediaPipe**

This project monitors a person's eyes through a webcam to detect drowsiness. It uses **MediaPipe Face Mesh** for landmark detection and calculates **Eye Aspect Ratio (EAR)** to trigger an alarm when eyes stay closed for too long.

---

## 📌 Features

- Real-time webcam feed
- Facial landmark detection with MediaPipe
- Eye Aspect Ratio (EAR) calculation
- Alarm alert on drowsiness
- Modular code structure for easy extension

---

## 🛠️ Tech Stack

- Python 3.10+
- OpenCV
- MediaPipe
- NumPy
- playsound

---

## 📁 Project Structure

```
drowsiness-detection/
│
├── main.py
├── config.py
├── utils/
│   ├── eye_utils.py
│   └── alert_utils.py
├── assets/
│   └── alarm.wav
├── README.md
└── .gitignore
```

---

## 🚀 Installation & Setup

1. Clone the repo:

```bash
git clone https://github.com/16Madhubala/drowsiness-detection.git
cd drowsiness-detection
```

2. Create and activate virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install opencv-python mediapipe numpy playsound==1.2.2
```

---

## ▶️ Run the Project

```bash
python main.py
```

- Close your eyes for ~2 seconds → alarm triggers
- Press **Q** to quit

---

## ⚙️ Configuration

Tweak `config.py` for your needs:

```python
EAR_THRESHOLD = 0.25    # Eye closed detection threshold
CONSEC_FRAMES = 20      # Frames before alarm triggers
ALARM_PATH = "assets/alarm.wav"
```

---

## 📸 Demo / Screenshots

*(Add screenshots or GIF here)*

---

## ⚠️ Notes & Tips

- Works best in good lighting
- Webcam quality affects accuracy
- Adjust thresholds per user for best results

---

## 📬 Contact

Created by **Madhubala (16Madhubala)**  
Happy coding! 😁
