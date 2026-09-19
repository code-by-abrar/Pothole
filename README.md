# 🛣️ Real-Time Pothole Detection using YOLOv8

An AI-powered computer vision system designed to detect road potholes in real time from video feeds and images, helping improve road safety and infrastructure maintenance.

---

## 🎥 Live Demo

Check out the live demo video showcasing the model in action:
- 🔗 **[LinkedIn Demo Video](https://lnkd.in/p/dXHSBCed)**
- 📁 **[Results Directory](./results/README.md)**

---

## 🚀 Features

- **Real-Time Detection:** Accurate pothole detection from videos and camera streams.
- **Cinematic Apple-Style Visualization:** Custom UI styling with semi-transparent label backgrounds and sleek bounding boxes.
- **Segmentation & Bounding Box Support:** High-precision localization of road damages.
- **Automated Video Export:** Saves rendered detection results into `results/output.mp4`.

---

## 📂 Project Structure

```
Pothole/
├── model/
│   └── best.pt             # Trained YOLOv8 model weights
├── results/
│   ├── README.md           # Demo link & results documentation
│   └── output.mp4          # Generated output video (after running inference)
├── src/
│   └── test5.py            # Main video detection & inference script
└── README.md
```

---

## ⚙️ Tech Stack

- **Python** (3.8+)
- **Ultralytics YOLOv8**
- **OpenCV**
- **NumPy**

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd Pothole
   ```

2. **Install dependencies:**
   ```bash
   pip install ultralytics opencv-python
   ```

3. **Verify model file:**
   Make sure `best.pt` is present inside the `model/` folder.

---

## 🎯 Usage

To run pothole detection on a video:

```bash
# Default (looks for video.mp4 in root and model in model/best.pt):
python src/test5.py

# Or pass custom video path:
python src/test5.py path/to/your_video.mp4
```

The annotated video will automatically be saved in:
`results/output.mp4`

---

## 👤 Author
**Abrar Ahmad**  
- [LinkedIn Profile](https://www.linkedin.com/in/abrar-ahmad-24045338b)
