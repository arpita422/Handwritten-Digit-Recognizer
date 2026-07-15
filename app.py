import tkinter as tk
from PIL import Image, ImageDraw
import numpy as np
from tensorflow.keras.models import load_model


model = load_model("model.h5")


root = tk.Tk()
root.title("Digit Predictor")
root.geometry("400x450")
root.resizable(False, False)


canvas = tk.Canvas(root, width=280, height=280, bg="black", cursor="cross")
canvas.pack(pady=20)

image = Image.new("L", (280, 280), "black")
draw_image = ImageDraw.Draw(image)

last_x = None
last_y = None


def start_draw(event):
    global last_x, last_y
    last_x = event.x
    last_y = event.y


def draw(event):
    global last_x, last_y

    canvas.create_line(
        last_x,
        last_y,
        event.x,
        event.y,
        fill="white",
        width=18,
        capstyle=tk.ROUND,
        smooth=True,
    )

    draw_image.line(
        (last_x, last_y, event.x, event.y),
        fill="white",
        width=18,
    )

    last_x = event.x
    last_y = event.y


canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)


def predict_digit():
    small = image.resize((28, 28))
    img = np.array(small)
    img = img / 255.0
    img = img.reshape(1, 28, 28, 1)

    prediction = model.predict(img, verbose=0)
    digit = np.argmax(prediction)
    confidence = np.max(prediction) * 100

    result_label.config(text=f"Prediction: {digit} ({confidence:.2f}%)")


def clear_canvas():
    global image, draw_image

    canvas.delete("all")

    image = Image.new("L", (280, 280), "black")
    draw_image = ImageDraw.Draw(image)
    result_label.config(text="Prediction: -")


result_label = tk.Label(root, text="Prediction: -", font=("Arial", 16))
result_label.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

predict_btn = tk.Button(button_frame, text="Predict", command=predict_digit, width=10)
predict_btn.pack(side=tk.LEFT, padx=10)

clear_btn = tk.Button(button_frame, text="Clear", command=clear_canvas, width=10)
clear_btn.pack(side=tk.LEFT, padx=10)

root.mainloop()