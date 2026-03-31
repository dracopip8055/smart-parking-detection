SmartPark AI: Parking Space Detection System
<div align="center">

An intelligent Computer Vision system that automatically detects available and occupied parking spaces from images or video streams in real-time.

Features
 • Quick Start
 • Architecture
 • Results

</div>
Problem Statement

In modern cities, drivers spend a significant amount of time searching for parking spaces. This leads to:

Traffic congestion
Fuel wastage
Time loss
Poor parking management

Manual monitoring of parking spaces is inefficient and not scalable. There is a need for an automated parking detection system that can monitor parking areas and detect available spaces in real-time.

Solution Overview

SmartPark AI is a Computer Vision-based system that analyzes parking lot images or video frames and automatically detects whether a parking slot is occupied or empty.

The system:

Detects parking slots
Determines occupancy status
Displays available parking count
Highlights empty and occupied slots visually

This system can be used in:

Shopping malls
Universities
Office buildings
Public parking areas
Smart cities
Key Features
Parking Slot Detection
Manual slot marking using mouse clicks
Slot coordinates stored for future detection
Works on images and video streams
Occupancy Detection
Image preprocessing (grayscale, blur, thresholding)
Pixel intensity analysis for each slot
Threshold-based classification:
Green → Empty
Red → Occupied
Real-Time Visualization
Bounding boxes drawn on parking slots
Displays number of available spaces
Real-time detection from video
Lightweight System
Runs on CPU
No GPU required
Fast and efficient
System Architecture
Input Image / Video
        │
        ▼
Image Preprocessing
(Grayscale → Blur → Threshold)
        │
        ▼
Parking Slot Extraction
(Using stored coordinates)
        │
        ▼
Pixel Analysis per Slot
        │
        ▼
Classification
(Occupied / Empty)
        │
        ▼
Visualization
(Bounding Boxes + Slot Count)
Tech Stack
Component	Technology
Programming Language	Python
Computer Vision	OpenCV
Numerical Computing	NumPy
Data Storage	Pickle (parking_slots.pkl)
Visualization	OpenCV Drawing
Project Structure
SmartPark-AI/
├── main.py                 # Main detection script
├── slot_marker.py          # Tool to mark parking slots
├── parking_slots.pkl       # Stored slot coordinates
├── requirements.txt        # Dependencies
├── images/                 # Parking images
├── videos/                 # Parking videos
├── output/                 # Output results
└── README.md               # Documentation
Installation
Prerequisites
Python 3.8+
pip
OpenCV
NumPy
Setup
git clone https://github.com/your-username/SmartPark-AI.git
cd SmartPark-AI

python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate

pip install -r requirements.txt
Quick Start
Step 1 — Mark Parking Slots
python slot_marker.py
Click on parking slot corners
Coordinates will be saved in parking_slots.pkl
Step 2 — Run Detection
python main.py

The system will:

Detect occupied and empty slots
Show available slot count
Display visual output
Results
Condition	Result
Well-lit environment	High accuracy
Shadows present	Medium accuracy
Night / Low light	Lower accuracy
Example Output
Free Slots: 8 / 12
Green Box → Empty
Red Box → Occupied
Challenges Faced
Lighting variations affected detection
Threshold tuning required
Manual slot marking takes time
Shadows sometimes detected as vehicles
Future Improvements
Automatic parking slot detection
Deep learning model (YOLO) for vehicle detection
Cloud dashboard for monitoring
Mobile app integration
CCTV real-time integration
Smart city deployment
Learning Outcomes

This project helped in understanding:

Image preprocessing techniques
Thresholding and morphological operations
Pixel-based object detection
Real-time computer vision systems
End-to-end project development
Conclusion

SmartPark AI demonstrates how Computer Vision can be used to solve real-world parking problems. The system is simple, efficient, and can be extended into a full smart parking management solution using deep learning and cloud technologies.

License

This project is licensed under the MIT License.

Author

Harsh Dhoriyani
Computer Science (AI & ML)
VIT Bhopal University
