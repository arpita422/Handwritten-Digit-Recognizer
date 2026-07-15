import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

model = load_model("model.h5")

def predict():
    print("Predict button clicked")

    img = image.resize((28, 28), Image.Resampling.LANCZOS)
    img.save("processed.png")

    img = np.array(img)

    img = 255 - img
    img = img.astype("float32") / 255.0
    img = img.reshape(1, 28, 28, 1)

    prediction = model.predict(img, verbose=0)

    print(prediction)

    digit = np.argmax(prediction)
    confidence = np.max(prediction) * 100

    print("Digit:", digit)
    print("Confidence:", confidence)

    result.config(text=f"Prediction: {digit}\nConfidence: {confidence:.2f}%")