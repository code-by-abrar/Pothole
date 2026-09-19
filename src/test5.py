import os
import sys
from pathlib import Path
import cv2
import numpy as np
from ultralytics import YOLO

# -------------------------------------------------------------
# 📁 Path Configurations
# -------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

# Search for model weights (check model/best.pt first, then root/src)
MODEL_CANDIDATES = [
    PROJECT_ROOT / "model" / "best.pt",
    PROJECT_ROOT / "best.pt",
    SCRIPT_DIR / "best.pt",
    Path("best.pt"),
]

model_path = next((p for p in MODEL_CANDIDATES if p.exists()), None)
if model_path is None:
    # Default fallback to expected location
    model_path = PROJECT_ROOT / "model" / "best.pt"

# Input video (command line argument or default video.mp4)
if len(sys.argv) > 1:
    video_source = sys.argv[1]
else:
    # Try video.mp4 in project root or current directory
    if (PROJECT_ROOT / "video.mp4").exists():
        video_source = str(PROJECT_ROOT / "video.mp4")
    elif Path("video.mp4").exists():
        video_source = "video.mp4"
    else:
        video_source = str(PROJECT_ROOT / "video.mp4")

# Output directory & video path
RESULTS_DIR = PROJECT_ROOT / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
output_video_path = RESULTS_DIR / "output.mp4"

# -------------------------------------------------------------
# 🤖 Load YOLO Model
# -------------------------------------------------------------
print(f"[*] Loading model from: {model_path}")
if not model_path.exists():
    print(f"[-] Warning: Model file not found at '{model_path}'.")
    print("    Please ensure 'best.pt' is placed inside the 'model/' directory.")
    sys.exit(1)

model = YOLO(str(model_path))

# -------------------------------------------------------------
# 🎥 Input Video Setup
# -------------------------------------------------------------
print(f"[*] Opening video source: {video_source}")
cap = cv2.VideoCapture(video_source)

if not cap.isOpened():
    print(f"[-] Error: Could not open video file or stream: '{video_source}'")
    print("[-] Please provide a valid video path. Usage:")
    print("    python src/test5.py [path_to_video.mp4]")
    sys.exit(1)

# Retrieve video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
if fps <= 0 or fps != fps:
    fps = 30.0

total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"[*] Video Resolution: {width}x{height} @ {fps:.1f} FPS (Total frames: {total_frames})")

# -------------------------------------------------------------
# 💾 Video Writer Setup
# -------------------------------------------------------------
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(str(output_video_path), fourcc, fps, (width, height))
print(f"[*] Saving detection output to: {output_video_path}")

# 🎨 Color palette (Apple style theme)
BOX_COLOR = (0, 122, 255)     # Vibrant iOS Blue (BGR)
TEXT_COLOR = (255, 255, 255)   # White
BG_COLOR = (20, 20, 20)        # Dark Slate for label badge
ALPHA = 0.65                   # Label transparency

frame_idx = 0
print("[*] Processing started... Press 'q' or 'ESC' on the preview window to exit early.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_idx += 1

    # Run inference
    results = model(frame, verbose=False)[0]

    # Pre-copy frame once for label transparency overlay if detections exist
    if len(results.boxes) > 0:
        overlay = frame.copy()
        labels_to_draw = []

        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls_id = int(box.cls[0])

            # Class name if available
            class_name = model.names[cls_id] if hasattr(model, "names") and cls_id in model.names else "Pothole"
            label = f"{class_name} {conf:.2f}"

            # 🔲 Draw bounding box directly on frame
            cv2.rectangle(frame, (x1, y1), (x2, y2), BOX_COLOR, 3)

            # 📝 Calculate text dimensions for snug badge
            (text_w, text_h), baseline = cv2.getTextSize(
                label, cv2.FONT_HERSHEY_SIMPLEX, 0.55, 2
            )

            # Keep label within frame boundaries
            if y1 - text_h - 12 >= 0:
                badge_y1 = y1 - text_h - 12
                badge_y2 = y1
                text_y = y1 - 6
            else:
                badge_y1 = y1
                badge_y2 = y1 + text_h + 12
                text_y = y1 + text_h + 8

            badge_x1 = max(0, x1)
            badge_x2 = min(width, x1 + text_w + 14)

            # Draw background badge on overlay
            cv2.rectangle(overlay, (badge_x1, badge_y1), (badge_x2, badge_y2), BG_COLOR, -1)

            # Store text info to draw after blending
            labels_to_draw.append((label, badge_x1 + 6, text_y))

        # 🧱 Alpha blend badges onto frame in one operation per frame
        cv2.addWeighted(overlay, ALPHA, frame, 1.0 - ALPHA, 0, frame)

        # 📝 Draw crisp text on top of blended badges
        for lbl, tx, ty in labels_to_draw:
            cv2.putText(
                frame,
                lbl,
                (tx, ty),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.55,
                TEXT_COLOR,
                2,
                cv2.LINE_AA,
            )

    # 💾 Write frame to output video
    out.write(frame)

    # 👁 Live preview window
    cv2.imshow("Cinematic Pothole Detection", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord("q"):
        print("\n[!] User interrupted processing.")
        break

# -------------------------------------------------------------
# 🧹 Cleanup & Summary
# -------------------------------------------------------------
cap.release()
out.release()
cv2.destroyAllWindows()

print("\n" + "=" * 50)
print(f"[✓] Processing complete! Processed {frame_idx} frames.")
print(f"[✓] Output saved to: {output_video_path}")
print("=" * 50)