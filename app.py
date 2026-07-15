import tkinter as tk
from PIL import Image, ImageDraw
import numpy as np
from tensorflow.keras.models import load_model

# Load trained model
model = load_model("model.h5")

# Create window
root = tk.Tk()
root.title("Handwritten Digit Recognizer")
root.geometry("320x420")

# Canvas
canvas = tk.Canvas(root, width=280, height=280, bg="white")
canvas.pack(pady=10)

# PIL image for drawing
image = Image.new("L", (280, 280), "white")
draw = ImageDraw.Draw(image)

# Draw on canvas
def paint(event):
    x, y = event.x, event.y
    r = 12
    canvas.create_oval(
        x-r, y-r, x+r, y+r,
        fill="black",
        outline="black"
    )
    draw.ellipse(
        (x-r, y-r, x+r, y+r),
        fill="black"
    )

canvas.bind("<B1-Motion>", paint)

# Predict digit
def predict():
    try:
        img = image.resize((28, 28), Image.Resampling.LANCZOS)

        img.save("processed.png")

        img = np.array(img)

        img = 255 - img
        img = img.astype("float32") / 255.0

        img = img.reshape(1, 28, 28, 1)

        prediction = model.predict(img, verbose=0)

        digit = np.argmax(prediction)
        confidence = np.max(prediction) * 100

        print("Prediction:", prediction)
        print("Digit:", digit)

        result.config(
            text=f"Prediction: {digit}\nConfidence: {confidence:.2f}%"
        )

    except Exception as e:
        print(e)
        result.config(text=str(e))
    

# Clear canvas
def clear():
    canvas.delete("all")
    draw.rectangle((0, 0, 280, 280), fill="white")
    result.config(text="Prediction:")

# Buttons
predict_btn = tk.Button(
    root,
    text="Predict",
    command=predict,
    width=15,
    height=2
)
predict_btn.pack(pady=5)

clear_btn = tk.Button(
    root,
    text="Clear",
    command=clear,
    width=15,
    height=2
)
clear_btn.pack(pady=5)

# Result label
result = tk.Label(
    root,
    text="Prediction:",
    font=("Arial", 18)
)
result.pack(pady=10)

root.mainloop()