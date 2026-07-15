# Handwritten-Digit-Recognizer
Turn your handwritten digits into AI predictions! This project uses a Convolutional Neural Network (CNN) and an intuitive Tkinter GUI to recognize handwritten digits in real time. Draw any digit on the canvas, and the trained model instantly predicts it with high accuracy using the MNIST dataset, demonstrating deep learning in action.
 📖 Overview

The Handwritten Digit Recognizer is a desktop application that recognizes handwritten digits (0–9) using a Convolutional Neural Network (CNN). The model is trained on the MNIST dataset, a widely used benchmark dataset containing 70,000 handwritten digit images.

The application provides a simple graphical user interface (GUI) where users can draw digits using a mouse. Once the digit is drawn, the trained model processes the image and predicts the corresponding digit in real time.

This project is suitable for beginners who want to learn about:

- Deep Learning
- Convolutional Neural Networks (CNN)
- Image Processing
- Computer Vision
- GUI Development using Tkinter
- TensorFlow & Keras

---

✨ Features

- Interactive GUI built with Tkinter
- Draw handwritten digits using the mouse
- CNN model trained on the MNIST dataset
- Real-time digit prediction
- Easy-to-use interface
- Beginner-friendly source code
- Modular project structure
- Lightweight desktop application

---

 🛠 Technologies Used

- Python 3.x
- TensorFlow
- Keras
- NumPy
- Pillow (PIL)
- Tkinter
- MNIST Dataset

---

 📋 Prerequisites

Before running the project, ensure the following software is installed:

- Python 3.9 or above
- Visual Studio Code (Recommended)
- Git (Optional)

Check your Python version:

```bash
python --version
```

---

 📦 Dependencies

Install all required libraries:

```bash
pip install tensorflow numpy pillow
```

Or install using:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`

```
tensorflow
numpy
Pillow
```

---

📁 Project Structure

```
Handwritten-Digit-Recognizer/
│
├── app.py               # GUI Application
├── train.py             # CNN Model Training
├── predict.py           # Prediction Script
├── model.h5             # Trained Model (Generated after training)
├── requirements.txt
├── README.md
└── .gitignore
```

---

 ⚙️ Setup

## Step 1

Clone the repository

```bash
git clone https://github.com/yourusername/Handwritten-Digit-Recognizer.git
```

## Step 2

Open the project

```bash
cd Handwritten-Digit-Recognizer
```

## Step 3

Install dependencies

```bash
pip install -r requirements.txt
```

---

 🧠 Training the Model

Train the CNN model using the MNIST dataset.

Run:

```bash
python train.py
```

During training, TensorFlow will download the MNIST dataset automatically (if not already available).

After training completes successfully, the trained model will be saved as:

```
model.h5
```

---

▶️ Running the GUI Application

Start the application:

```bash
python app.py
```

The application window will open.

### Steps

1. Draw a digit (0–9) on the canvas.
2. Click **Predict**.
3. The application displays the predicted digit.
4. Click **Clear** to erase the canvas and draw another digit.

---

🔍 Running Prediction

If you want to test prediction separately, run:

```bash
python predict.py
```

The script loads the trained model and predicts the handwritten digit.

---

 📊 Sample Output

```
Prediction : 8

Confidence : 99.24%
```

---
📚 How It Works

```
User Draws Digit
        │
        ▼
Tkinter Canvas
        │
        ▼
Image Preprocessing
        │
        ▼
Resize to 28 × 28
        │
        ▼
Normalize Image
        │
        ▼
CNN Model
        │
        ▼
Predicted Digit
```

---

🎯 Applications

- Optical Character Recognition (OCR)
- Digit Recognition Systems
- Educational AI Projects
- Computer Vision Learning
- Deep Learning Practice
- Image Classification
- Academic Demonstrations

---


---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
