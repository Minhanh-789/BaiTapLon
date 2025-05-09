# Tự Động Lấy Dữ Liệu Biệt Thự Đà Nẵng từ Alonhadat
Một công cụ Python giúp tự động thu thập dữ liệu các bài đăng bán biệt thự tại Đà Nẵng trên trang alonhadat.com.vn và lưu vào file CSV.

## Tính năng chính
Tự động mở trình duyệt và truy cập trang web bất động sản.
Thu thập thông tin tiêu đề, mô tả, địa chỉ, giá bán của từng biệt thự tại Đà Nẵng.
Lưu dữ liệu thành file CSV để tiện tra cứu.
Tự động chạy vào lúc 6:00 sáng mỗi ngày.

## Công nghệ sử dụng
Python 3
Selenium – Điều khiển trình duyệt tự động.
schedule – Lập lịch chạy định kỳ.
csv, time, sys – Xử lý dữ liệu và thời gian.

## Cấu trúc dự án
css
Sao chép
Chỉnh sửa
├── alonhadat.py                  # File chính chạy chương trình
├── requirements.txt         # Danh sách thư viện cần cài
└── alonhadat_bietthu_danang.csv  # File kết quả (tự động tạo sau khi chạy)

## Hướng dẫn cài đặt và sử dụng
### 1. Cài đặt thư viện cần thiết

```bash
pip install -r requirements.txt
```

### 2. Tải và cấu hình WebDriver
```bash
Tải ChromeDriver tại: https://chromedriver.chromium.org/downloads
```
Đảm bảo driver tương thích với phiên bản Chrome đang dùng.
Đặt chromedriver.exe vào thư mục PATH hoặc cùng thư mục với alonhadat.py.

### 3. Chạy chương trình
```bash
python main.py
