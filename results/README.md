# 🛣️ Pothole Detection - Results & Demo

This directory contains the detection outputs and links to live demonstrations of the AI-powered Pothole Detection model.

---

## 🎥 Live Demo Video

Watch the real-time AI detection in action on LinkedIn:
👉 **[Watch Live Demo on LinkedIn](https://lnkd.in/p/dXHSBCed)**

**Direct Post URL:**  
[https://www.linkedin.com/posts/abrar-ahmad-24045338b_ai-computervision-yolov8-activity-7440947057965686784-ADoJ](https://www.linkedin.com/posts/abrar-ahmad-24045338b_ai-computervision-yolov8-activity-7440947057965686784-ADoJ)

---

## 📌 Project Highlights
- **Model:** YOLOv8 trained for automated road pothole detection
- **Capabilities:** Real-time road damage detection with high precision
- **Visualization:** Apple-style cinematic bounding boxes, confidence scoring, and video rendering
- **Output:** Annotated video saved directly to `results/output.mp4`

---

## 💻 How to Generate Results Locally

1. Place your test video (e.g. `video.mp4`) in the project root or specify its path.
2. Ensure model weights are located at `model/best.pt`.
3. Run the inference script:
   ```bash
   python src/test5.py
   ```
   Or specify a custom video path:
   ```bash
   python src/test5.py path/to/your_input_video.mp4
   ```
4. The generated output video with detections will be saved to:
   ```
   results/output.mp4
   ```
