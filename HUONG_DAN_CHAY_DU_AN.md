# Hướng Dẫn Chạy Dự Án ERPNext

## ✅ Đã Cài Đặt Thành Công

Dự án ERPNext đã được cài đặt và đang chạy trên WSL2 Ubuntu!

## 🌐 Truy Cập Ứng Dụng

### Từ Windows:
- **URL**: http://172.31.137.203:8000
- **Hoặc**: http://localhost:8000 (nếu port forwarding hoạt động)

### Thông Tin Đăng Nhập:
- **Username**: Administrator
- **Password**: (Sử dụng password admin từ database server)

## 📁 Cấu Trúc Dự Án

```
~/frappe-bench/                    # Thư mục chính trong WSL
├── apps/
│   ├── frappe/                    # Frappe Framework (v15)
│   └── erpnext/                   # ERPNext App (v16)
├── sites/
│   └── erpnext.localhost/         # Site của bạn
│       └── site_config.json       # Cấu hình database
└── config/                        # Cấu hình bench
```

## 🗄️ Cấu Hình Database

Đã kết nối với MariaDB server từ xa:


## 🚀 Các Lệnh Quan Trọng

### Khởi động server (đã chạy):
```bash
wsl -d Ubuntu bash -c "cd ~/frappe-bench && bench start"
```

### Dừng server:
Nhấn `Ctrl+C` trong terminal đang chạy bench

### Kiểm tra trạng thái:
```bash
wsl -d Ubuntu bash -c "cd ~/frappe-bench && bench --site erpnext.localhost list-apps"
```

### Cập nhật code:
```bash
wsl -d Ubuntu bash -c "cd ~/frappe-bench && bench update"
```

### Build assets:
```bash
wsl -d Ubuntu bash -c "cd ~/frappe-bench && bench build"
```

### Xem logs:
```bash
wsl -d Ubuntu bash -c "cd ~/frappe-bench && bench --site erpnext.localhost console"
```

## 🔧 Phát Triển

### Chỉnh sửa code:
- Code ERPNext nằm trong: `~/frappe-bench/apps/erpnext/` (trong WSL)
- Bạn có thể edit từ Windows bằng VS Code với WSL extension
- Hoặc mount thư mục: `\\wsl$\Ubuntu\home\chinhlt\frappe-bench\apps\erpnext`

### Restart sau khi sửa code Python:
```bash
# Bench tự động reload khi file Python thay đổi
# Nếu cần restart thủ công:
wsl -d Ubuntu bash -c "cd ~/frappe-bench && bench restart"
```

### Build lại assets sau khi sửa JS/CSS:
```bash
wsl -d Ubuntu bash -c "cd ~/frappe-bench && bench build --app erpnext"
```

## 📝 Ghi Chú

- **Frappe Version**: v15.89.0
- **ERPNext Version**: v16 (có warning về version mismatch nhưng vẫn chạy được)
- **Redis**: Đang chạy local trên WSL
- **MariaDB**: Kết nối remote server

## ⚠️ Lưu Ý

1. Database đã có dữ liệu từ trước, không phải database mới
2. Encryption key đã được tạo mới - nếu cần decrypt dữ liệu cũ, cần lấy key từ server gốc
3. Server chạy ở chế độ development (không dùng cho production)

## 🐛 Troubleshooting

### Không truy cập được từ Windows:
```bash
# Kiểm tra IP của WSL
wsl -d Ubuntu bash -c "hostname -I"

# Thử truy cập: http://<IP_WSL>:8000
```

### Port bị chiếm:
```bash
# Kiểm tra process đang dùng port
wsl -d Ubuntu bash -c "sudo lsof -i :8000"
```


## 📞 Hỗ Trợ

Nếu gặp vấn đề, kiểm tra logs:
```bash
wsl -d Ubuntu bash -c "tail -f ~/frappe-bench/sites/erpnext.localhost/logs/web.log"
```
