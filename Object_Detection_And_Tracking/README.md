# 🚀 Object Detection and Tracking using YOLOv8 + SORT

## 📌 Overview
This project implements a real-time object detection and tracking system using:

- YOLOv8 for object detection  
- SORT (Simple Online Realtime Tracking) for tracking objects across frames  
- OpenCV for video processing  

The system detects objects from a webcam or video and assigns unique IDs to track them in real time.

---

## 🎯 Features
- 🎥 Real-time webcam/video input  
- 🧠 Object detection using YOLOv8  
- 🔁 Object tracking with unique IDs (SORT)  
- 📦 Lightweight and fast  
- 🖥️ Live visualization with bounding boxes  

---

## 🛠️ Tech Stack
- Python  
- OpenCV  
- YOLOv8 (Ultralytics)  
- SORT Algorithm  
- NumPy  

---

## 📂 Project Structure
```
object_tracking_project/
 ├── main.py        # Main application
 ├── sort.py        # SORT tracking algorithm
 └── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository
```
git clone https://github.com/your-username/object-tracking.git
cd object-tracking
```

### 2. Install dependencies
```
pip install opencv-python ultralytics numpy filterpy scipy
```

---

## ▶️ Usage

Run the project:

```
python main.py
```

### Controls:
- Press ESC or Q to exit

---

## 🎥 Output
- Webcam window opens  
- Objects are detected in real time  
- Each object is assigned a unique ID  
- Bounding boxes are drawn around objects  

---

## 🧠 How It Works

1. YOLOv8 detects objects in each frame  
2. Detected bounding boxes are passed to SORT  
3. SORT assigns IDs and tracks movement  
4. OpenCV displays results in real time  

---

## 🚀 Future Improvements
- Use Deep SORT for better tracking accuracy  
- Add object counting (e.g., people counter)  
- Save output video  
- Improve UI  

---

## 📜 License
This project uses the SORT algorithm by Alex Bewley, licensed under the GNU General Public License.

---

## 🙌 Acknowledgements

This project is built using the following open-source technologies:

- YOLOv8 by Ultralytics  
  https://github.com/ultralytics/ultralytics  

- SORT: Simple Online and Realtime Tracking by Alex Bewley  
  https://github.com/abewley/sort  

- OpenCV  
  https://opencv.org/  

Special thanks to the open-source community for making these tools freely available.


## 💡 Author
**Palak Bharat Paryani**

## 🏢 Internship
**AI Internship - CodeAlpha**
