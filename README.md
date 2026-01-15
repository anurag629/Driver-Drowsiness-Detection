---
title: DrowseGuard - Driver Drowsiness Detection
emoji: 🛡️
colorFrom: blue
colorTo: blue
sdk: streamlit
sdk_version: "1.36.0"
app_file: main.py
pinned: false
license: mit
---

# 🛡️ DrowseGuard - Driver Drowsiness Detection

<div align="center">

**Real-time driver fatigue monitoring system using computer vision**

[![Streamlit](https://img.shields.io/badge/Streamlit-1.36.0-FF4B4B.svg)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[🎥 Live Demo](#) | [📖 Documentation](#usage) | [🚀 Deploy Your Own](#deployment)

</div>

---

## 🎯 About

**DrowseGuard** is an intelligent driver drowsiness detection system that monitors eye movements in real-time to detect fatigue and prevent accidents. Using advanced computer vision and the Eye Aspect Ratio (EAR) algorithm, it provides instant alerts when drowsiness is detected.

### ✨ Key Features

- 🎥 **Real-time Detection** - WebRTC-based browser video processing
- 👁️ **Eye Aspect Ratio (EAR)** - Scientifically validated drowsiness metric
- 🔔 **Multi-modal Alerts** - Visual overlays + audio warnings
- ⚙️ **Configurable Sensitivity** - Adjustable thresholds for personalized detection
- 📊 **Live Dashboard** - Monitor EAR values, alerts, and session time
- 🎨 **Modern UI** - Clean, dark-themed interface
- 🌐 **Browser-based** - No installation required, works in any modern browser

---

## 🚀 Quick Start

### Using This Space

1. **Click START** in the video feed section
2. **Grant webcam permission** when prompted by your browser
3. **Position your face** in front of the camera
4. The system will automatically:
   - Detect your face and eyes
   - Draw green contours around eyes
   - Monitor your Eye Aspect Ratio (EAR)
   - Alert you if drowsiness is detected (💤 + sound)

### ⚙️ Configuration

Adjust detection sensitivity using the sliders in the **Configuration** panel:

| Setting | Range | Default | Description |
|---------|-------|---------|-------------|
| **EAR Sensitivity** | 0.15 - 0.35 | 0.25 | Lower = more sensitive detection |
| **Alert Delay** | 5 - 50 frames | 20 | Frames before triggering alert |

**Tips:**
- **Increase sensitivity** (lower EAR) for earlier warnings
- **Decrease sensitivity** (higher EAR) to reduce false positives
- **Reduce frames** for faster alerts (but more false alarms)

---

## 🧠 How It Works

### Eye Aspect Ratio (EAR) Algorithm

The system calculates the Eye Aspect Ratio using facial landmarks:

```
EAR = (||p2 - p6|| + ||p3 - p5||) / (2 * ||p1 - p4||)
```

Where `p1-p6` are the 6 facial landmark points for each eye.

### Detection Pipeline

1. **Face Detection** → dlib's HOG-based frontal face detector
2. **Landmark Extraction** → 68-point facial landmark predictor
3. **EAR Calculation** → Compute eye openness for both eyes
4. **Threshold Check** → Compare against configurable threshold (default: 0.25)
5. **Alert Trigger** → If EAR < threshold for 20+ consecutive frames
6. **Multi-modal Alert** → Visual overlay + audio warning

**Why EAR?** When eyes close, the vertical eye distance decreases while horizontal distance remains constant, causing EAR to drop significantly (~40% reduction).

---

## 📊 Dashboard Metrics

### Status Indicator
- **👁️ ACTIVE** - System monitoring (green)
- **💤 DROWSINESS!** - Alert triggered (red)
- **📷 STANDBY** - Camera not active (gray)

### Real-time Metrics
- **Eye Aspect Ratio** - Current EAR value (cyan)
- **Total Alerts** - Cumulative alert count
- **Session Time** - Elapsed monitoring time (HH:MM:SS)

---

## 🛠️ Technical Stack

| Component | Technology |
|-----------|------------|
| **Framework** | Streamlit 1.36.0 |
| **Video Streaming** | streamlit-webrtc, WebRTC |
| **Computer Vision** | OpenCV, dlib |
| **Face Detection** | dlib frontal face detector |
| **Landmarks** | 68-point facial landmark predictor |
| **Scientific Computing** | NumPy, SciPy |

---

## ⚠️ Important Notes

### Browser Compatibility
- ✅ **Chrome/Edge** (recommended)
- ✅ **Firefox**
- ⚠️ **Safari** (may have WebRTC issues)
- ❌ **Internet Explorer** (not supported)

### Privacy & Security
- ✅ All video processing happens **locally in your browser**
- ✅ **No video data** is sent to servers or stored
- ✅ **No data collection** or analytics
- ✅ Webcam access controlled by browser permissions

### Legal Disclaimer
> ⚠️ **This is a demonstration tool for educational purposes.** It should NOT be used as the sole safety mechanism in vehicles. Always prioritize adequate rest and avoid driving when fatigued. This tool does not replace professional medical advice or vehicle safety systems.

---

## 🎓 Use Cases

- 🚛 **Long-distance Truckers** - Monitor fatigue during extended drives
- 🚗 **Daily Commuters** - Safety during routine travel
- 🏢 **Fleet Management** - Monitor commercial drivers
- 🔬 **Research** - Study drowsiness patterns and interventions
- 📚 **Education** - Learn computer vision and real-time ML

---

## 📝 Local Development

### Prerequisites
- Python 3.8+
- Webcam
- Modern browser

### Installation

```bash
# Clone repository
git clone https://huggingface.co/spaces/YOUR_USERNAME/drowseguard
cd drowseguard

# Install dependencies
pip install -r requirements.txt

# Download dlib model (if not included)
# Place shape_predictor_68_face_landmarks.dat in models/

# Run application
streamlit run main.py
```

### File Structure
```
drowseguard/
├── main.py                  # Main application
├── requirements.txt         # Dependencies
├── README.md               # This file
├── assets/
│   ├── style.css           # Custom UI styling
│   └── *.jpg/png           # Sample images
├── models/
│   └── shape_predictor_68_face_landmarks.dat  # Facial landmark model
└── music.wav               # Alert sound
```

---

## 🤝 Contributing

Contributions welcome! Areas for improvement:

- [ ] Multi-metric detection (yawn, head pose, blink rate)
- [ ] Mobile responsive layout
- [ ] Alert history logging and analytics
- [ ] Calibration phase for personalized thresholds
- [ ] Multiple language support
- [ ] Offline mode support

---

## 📚 References

- **EAR Algorithm**: Soukupová, T., & Čech, J. (2016). Real-Time Eye Blink Detection using Facial Landmarks.
- **dlib Library**: [http://dlib.net/](http://dlib.net/)
- **Streamlit-WebRTC**: [https://github.com/whitphx/streamlit-webrtc](https://github.com/whitphx/streamlit-webrtc)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **dlib** for facial landmark detection
- **Streamlit** for the amazing web framework
- **streamlit-webrtc** for browser video streaming
- Computer vision research community

---

<div align="center">

**⭐ If you find this useful, please star the Space! ⭐**

Made with ❤️ using Streamlit

[🐛 Report Bug](https://huggingface.co/spaces/YOUR_USERNAME/drowseguard/discussions) | [💡 Request Feature](https://huggingface.co/spaces/YOUR_USERNAME/drowseguard/discussions)

</div>
