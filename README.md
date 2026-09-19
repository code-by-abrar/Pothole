# 🛣️ RoadGuard AI — Pothole & Road Hazard Detection System

<div align="center">

[![YOLOv8](https://img.shields.io/badge/YOLOv8-Object%20Detection-blue.svg?style=for-the-badge)](https://ultralytics.com)
[![PyTorch](https://img.shields.io/badge/PyTorch-Computer%20Vision-EE4C2C.svg?style=for-the-badge&logo=pytorch)](https://pytorch.org)
[![Smart Cities](https://img.shields.io/badge/Smart%20Cities-Civil%20Safety-FF9800.svg?style=for-the-badge)](https://github.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

**Automated road surface defect detection model identifying potholes and road cracks from vehicular dashcams to streamline municipal maintenance.**

</div>

---

## 📌 Overview

Potholes cause millions in vehicle damages and hazardous accidents every year. **RoadGuard AI** provides municipal authorities and navigation providers with automated road defect localization from standard camera feeds.

---

## ⚡ Key Features

- **🕳️ Pothole Localization**: Detects depth craters and surface depressions under varying asphalt conditions.
- **🚗 Dashcam Integration**: Engineered for moving vehicle camera recordings.
- **⚡ Fast Inference**: Capable of 30+ FPS processing on edge GPU devices.

---

## 🛠️ Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Detection Test**:
   ```bash
   python src/test5.py
   ```

---

## 📂 Structure

```text
Pothole/
├── model/
│   └── best.pt               # Trained pothole detection model
├── results/                  # Training performance metrics
├── src/
│   └── test5.py              # Test inference script
├── requirements.txt          # Python dependencies
├── LICENSE                   # Apache 2.0 License
└── README.md
```

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.
