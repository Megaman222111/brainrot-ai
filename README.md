# Brainrot AI – Real-Time Meme Emotion Classifier

## Overview
**Brainrot AI** is a real-time computer vision project that classifies live webcam footage into distinct “brainrot” meme emotions using a **custom-trained FastAI convolutional neural network (CNN)** and **OpenCV**.  
The model was trained from scratch on a curated dataset of meme imagery, learning to identify emotion patterns such as “locked in,” “shocked,” “freaky,” and “tongue.”  
It combines deep learning with real-time computer vision to analyze and visualize meme culture dynamics.

---

## Features
- **Self-Trained Deep Learning Model** – Built and trained from scratch using **FastAI** and **PyTorch**.  
- **Real-Time Inference** – Processes webcam frames live and displays predicted emotion labels with confidence scores.  
- **Dynamic Visualization** – Shows the webcam feed alongside static “reaction” images representing each detected emotion.  
- **OpenCV Integration** – Handles all video capture, frame manipulation, and visualization logic.  
- **Lightweight Execution** – Fully Python-based, requiring no web frameworks or servers.  

---

## Tech Stack
**Languages:** Python  
**Libraries and Frameworks:**
- **FastAI** – Model training and inference  
- **PyTorch** – Deep learning backend  
- **OpenCV** – Webcam capture and visualization  
- **NumPy** – Matrix and image data handling  
- **Pillow (PIL)** – Frame conversion and preprocessing
