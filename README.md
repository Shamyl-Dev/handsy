# ✋🔊 Handsy

Control your PC volume using just your fingers — no keyboard, no mouse, just hands.

Handsy is a computer vision project built with Python, OpenCV, and MediaPipe. It detects how many fingers you have raised and adjusts your system volume accordingly.

---

## 📽️ Demo

<!-- Replace with actual screenshot or demo GIF -->
![Demo Screenshot](images/demo.gif)

---

## 🧠 How It Works

- Uses **MediaPipe** to track 21 hand landmarks in real-time via webcam  
- Identifies finger positions by comparing landmark coordinates  
- Maps the number of fingers raised to volume levels (e.g., 0 fingers = mute, 5 fingers = full volume)  
- Adjusts system volume dynamically using the `pycaw` library  

---

## 🛠️ Tech Stack

- **Python**  
- **OpenCV** — for video frame capture & drawing  
- **MediaPipe** — for real-time hand landmark detection  
- **pycaw** — for controlling system volume (Windows only)  

---

## 🚀 Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/handsy.git
   cd handsy
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the program:
   ```bash
   python handsy.py
   ```

> ⚠️ This program currently works only on Windows due to the volume control library used.

---

## 📷 Screenshots

<!-- Add images when ready -->
![Hand Detection](images/hand-detection.png)  
![Volume Control](images/volume-control.png)  

---

## 🧪 Features

- Real-time hand tracking with low latency  
- Automatic detection of how many fingers are raised  
- System volume smoothly adjusts based on your hand gestures  
- Easy to use and fun to demo  

---

## 🙋‍♂️ Why I Built This

Because I was eating wings and didn’t want to touch my keyboard.  
Also — because it was cool.

---

## 📄 License

MIT — do whatever you want, just don’t sue me.

---

## 🔗 Connect

Built by **Shamyl Khan**  
📧 knshamyl@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/shamylikhan/)
