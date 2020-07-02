# CryptoNetwork_192_Assignment
This project is our assignment of the class `Cryptography and Network security`.

## 1. Hướng dẫn cài đặt môi trường
#### Lưu ý: Hướng dẫn này được áp dụng với Windows
1. Tải `Python 3.8` từ địa chỉ `https://www.python.org/downloads/windows/`
2. Cài đặt như bình thường. Trong quá trình cài đặt, lưu ý cần tích vào ô **Add to PATH** để có thể chạy Python từ `cmd` hoặc `Powershell`.
3. Mở `cmd` hoặc `Powershell`, nhập lệnh sau:
   > pip install --user pipenv

   Lưu ý nếu câu lệnh trên không chạy được do thiếu `pip` thì có thể xem thêm cách cài `pip`

4. Trong folder code, mở `cmd` lên và nhập lệnh:
   > pipenv install
   Câu lệnh trên sẽ cài đặt các thư viện cần thiết cho việc phát triển.

## 2. Phân công công việc
### 2.1. Website
Mình sẽ đọc trực tiếp file `index.html` từ thư mục `thiswebsite`.

### 2.2. Cấu trúc thư mục
#### 2.2.1. Thư mục `testing_html`
Thư mục này sẽ chứa các file `html` dùng để kiểm tra thuật toán xem đúng chưa. Các file này sẽ mô phỏng kết quả khi bị tấn công và thay đổi giao diện.

Cách sử dụng: Copy paste nội dung của file test muốn thử và dán đè vào file `index.html` trong thư mục `thiswebsite`.

Em sẽ cập nhật các file này sau, hoặc anh có thể tự tạo test file cho mình

### 2.2.2. File `checkingModules.py`
Đây sẽ là file mọi người code. Trong đó đã phân rõ ràng hàm của từng người, quy định luôn input đầu vào là gì và giá trị trả về là gì.

### 2.2.3. File `defaultFootprint.json`
File này sẽ chứa các thông tin mà anh sẽ đối chiếu khi kiểm tra số lượng. Trong code em đã hiện thực sẵn phần code đọc file này nên anh chỉ cần sử dụng biến đó thôi.

### 2.3. Phân công
| Thành viên | Nhiệm vụ |
|:---|:---|
| Khoa Trần | Hiện thực code kiểm tra defaced bằng kiểm tra số lượng các tag và số lượng các ký tự |
| Hoàng Lê | Hiện thực code kiểm tra cấu trúc và kiểm tra sự bất thường |
