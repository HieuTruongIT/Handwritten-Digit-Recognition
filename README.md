## Handwritten Digit Recognition
Handwritten Digit Recognition là một ứng dụng sử dụng học máy và học sâu để nhận diện các chữ số viết tay từ bộ dữ liệu MNIST. Mô hình được xây dựng để nhận diện chữ số từ các hình ảnh số học viết tay và có thể ứng dụng trong nhiều lĩnh vực như nhận dạng chữ viết tay trong các hệ thống tự động, kiểm tra bài thi, hay nhận diện các mã vạch từ các tài liệu giấy.

![image](https://github.com/user-attachments/assets/862d54c7-230b-4358-b142-c481a9d95374)

Các bước thực hiện

1 - Thu thập dữ liệu:

Bộ dữ liệu MNIST bao gồm 60,000 hình ảnh huấn luyện và 10,000 hình ảnh kiểm tra, mỗi hình ảnh là một số viết tay có kích thước 28x28 pixel.
Tiền xử lý dữ liệu:

Dữ liệu được chuẩn hóa về phạm vi [0, 1] bằng cách chia mỗi pixel cho 255.
Các nhãn của dữ liệu được chuyển đổi thành dạng one-hot encoding.

2 - Xây dựng mô hình:

Mô hình học sâu sử dụng mạng nơ-ron (Neural Network) với các lớp Dense và lớp Flatten để chuyển đổi hình ảnh 2D thành dạng 1D.
Hàm kích hoạt ReLU được sử dụng cho các lớp ẩn, trong khi đó, hàm Softmax được dùng ở lớp đầu ra để phân loại 10 chữ số từ 0 đến 9.

3 - Huấn luyện mô hình:

Mô hình được huấn luyện với bộ dữ liệu MNIST, sử dụng thuật toán tối ưu Adam và hàm mất mát categorical cross-entropy.
Sau khi huấn luyện xong, mô hình sẽ được đánh giá trên bộ dữ liệu kiểm tra (test data).
## Ứng dụng nhận diện chữ số viết tay:

Sau khi huấn luyện, mô hình có thể được sử dụng để nhận diện chữ số viết tay từ người dùng qua giao diện vẽ.
Giao diện vẽ sử dụng thư viện Tkinter, cho phép người dùng vẽ các chữ số và mô hình sẽ đưa ra dự đoán.

## delevloper : Shinichi Kudo 
