import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image, ImageDraw, ImageOps
import sys
sys.stdout.reconfigure(encoding='utf-8')


# Bước 1: Tải bộ dữ liệu MNIST
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

# Bước 2: Chuẩn hóa dữ liệu
X_train, X_test = X_train / 255.0, X_test / 255.0  # Chia cho 255 để giá trị pixel nằm trong khoảng [0, 1]

# Bước 3: Chuyển đổi nhãn sang dạng one-hot encoding
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Bước 4: Xây dựng mô hình mạng nơ-ron
model = Sequential([
    Flatten(input_shape=(28, 28)),  # Chuyển hình ảnh 28x28 thành vector 784 phần tử
    Dense(128, activation='relu'),  # Lớp ẩn với 128 nơ-ron và hàm kích hoạt ReLU
    Dense(64, activation='relu'),   # Lớp ẩn thứ hai với 64 nơ-ron và hàm kích hoạt ReLU
    Dense(10, activation='softmax')  # Lớp đầu ra với 10 nơ-ron (tương ứng với 10 chữ số) và hàm Softmax
])

# Bước 5: Compile mô hình
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Bước 6: Huấn luyện mô hình
print("Dang huan luyen mo hinh...")
model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test), batch_size=32)
print("Huấn luyện xong!")

# Bước 7: Giao diện vẽ số
class DrawingApp:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        self.canvas = tk.Canvas(root, width=280, height=280, bg='white')
        self.canvas.pack()

        self.button_clear = tk.Button(root, text="Clear", command=self.clear_canvas)
        self.button_clear.pack(side=tk.LEFT)

        self.button_predict = tk.Button(root, text="Predict", command=self.predict_digit)
        self.button_predict.pack(side=tk.RIGHT)

        self.image = Image.new("L", (28, 28), color=255)  # Hình ảnh nền trắng 28x28
        self.draw = ImageDraw.Draw(self.image)
        self.canvas.bind("<B1-Motion>", self.paint)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (28, 28), color=255)  # Clear image
        self.draw = ImageDraw.Draw(self.image)

    def paint(self, event):
        x, y = event.x, event.y
        r = 10  # Bán kính cọ vẽ
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill='black')
        self.draw.ellipse([x//10-r//10, y//10-r//10, x//10+r//10, y//10+r//10], fill=0)  # Draw black

    def predict_digit(self):
        # Chuẩn bị hình ảnh cho dự đoán
        img_resized = self.image.resize((28, 28), Image.ANTIALIAS)
        img_array = np.array(img_resized) / 255.0  # Normalized between 0 and 1
        img_array = img_array.reshape(1, 28, 28)  # Add batch dimension

        # Dự đoán
        prediction = self.model.predict(img_array)
        predicted_digit = np.argmax(prediction)
        confidence = np.max(prediction)

        # Hiển thị kết quả
        print(f"Dự đoán: {predicted_digit}, Độ tin cậy: {confidence * 100:.2f}%")
        self.show_result(predicted_digit, confidence)

    def show_result(self, digit, confidence):
        result_window = tk.Toplevel(self.root)
        result_window.title("Kết quả dự đoán")
        tk.Label(result_window, text=f"Số dự đoán: {digit}\nĐộ tin cậy: {confidence * 100:.2f}%", font=("Arial", 16)).pack()

# Bước 8: Chạy giao diện
root = tk.Tk()
root.title("Handwritten Digit Recognition")
app = DrawingApp(root, model)
root.mainloop()
