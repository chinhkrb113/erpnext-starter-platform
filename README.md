# ERPNext - Hệ Thống ERP

**Tác giả:** Lê Thành Chỉnh  
**Phiên bản:** 16.x (Development)  
**Giấy phép:** GPL-3.0  
**Đối tượng:** Developer nội bộ, Sinh viên, Open-source Contributors

---

## 📋 Giới Thiệu

ERPNext là hệ thống hoạch định nguồn lực doanh nghiệp (ERP) mã nguồn mở, được xây dựng trên nền tảng Frappe Framework. Dự án này giải quyết các vấn đề quản lý doanh nghiệp toàn diện bao gồm:

- **Quản lý tài chính & kế toán**: Ghi nhận giao dịch, báo cáo tài chính, quản lý ngân sách
- **Quản lý bán hàng & mua hàng**: Đơn hàng, báo giá, hóa đơn, quản lý khách hàng/nhà cung cấp
- **Quản lý kho & sản xuất**: Theo dõi tồn kho, lập kế hoạch sản xuất, quản lý BOM
- **Quản lý dự án & nhân sự**: Timesheet, task management, quản lý nhân viên
- **CRM & Marketing**: Quản lý leads, campaigns, customer journey

### Vấn Đề Giải Quyết

Thay vì sử dụng nhiều phần mềm riêng lẻ cho từng chức năng, ERPNext cung cấp một nền tảng tích hợp duy nhất, giúp:
- Giảm chi phí phần mềm cho doanh nghiệp vừa và nhỏ
- Tích hợp dữ liệu giữa các phòng ban
- Tự động hóa quy trình nghiệp vụ
- Báo cáo và phân tích dữ liệu thời gian thực

---

## 🏗️ Kiến Trúc & Công Nghệ

### Stack Công Nghệ

**Backend:**
- Python 3.10+ (Core business logic)
- Frappe Framework 16.x (Web framework)
- MariaDB/PostgreSQL (Database)
- Redis (Cache & Queue)

**Frontend:**
- JavaScript/Vue.js (UI Components)
- Frappe UI Library (Component system)
- HTML/CSS/SCSS (Styling)

**Infrastructure:**
- Nginx (Web server - Production)
- Gunicorn (WSGI server)
- Supervisor (Process management)
- Docker (Containerization - Optional)

### Kiến Trúc Hệ Thống

```
┌─────────────────────────────────────────────────────────────┐
│                      Client Browser                          │
│                   (HTML/CSS/JavaScript)                      │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTP/HTTPS
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    Nginx (Reverse Proxy)                     │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              Frappe Framework (Python/WSGI)                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   ERPNext    │  │   Frappe     │  │   Custom     │      │
│  │   Modules    │  │   Core       │  │   Apps       │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└────────┬──────────────────┬──────────────────┬──────────────┘
         │                  │                  │
         ▼                  ▼                  ▼
┌─────────────────┐ ┌─────────────┐ ┌──────────────────┐
│   MariaDB       │ │   Redis     │ │  File Storage    │
│   (Database)    │ │ (Cache/Queue)│ │  (Attachments)   │
└─────────────────┘ └─────────────┘ └──────────────────┘
```

### Luồng Xử Lý Request

```
User Request → Nginx → Frappe Router → DocType Controller 
    → Database Query → Business Logic → Response → Client
```

---

## 🚀 Hướng Dẫn Cài Đặt & Chạy

### Yêu Cầu Hệ Thống

- **OS:** Ubuntu 20.04+, macOS, Windows (WSL2)
- **Python:** 3.10 hoặc cao hơn
- **Node.js:** 18.x hoặc 20.x
- **MariaDB:** 10.6+ hoặc PostgreSQL 12+
- **Redis:** 6.x+
- **RAM:** Tối thiểu 4GB (khuyến nghị 8GB+)
- **Disk:** 10GB+ dung lượng trống

### Phương Án 1: Cài Đặt Trên WSL2 (Windows)

#### Bước 1: Cài Đặt WSL2 & Ubuntu

```powershell
# Cài đặt WSL2
wsl --install

# Khởi động lại máy, sau đó kiểm tra
wsl --list --verbose
```

#### Bước 2: Cài Đặt Dependencies

```bash
# Trong WSL Ubuntu
sudo apt update
sudo apt install -y \
    git python3-dev python3-pip python3-venv \
    redis-server mariadb-server libmysqlclient-dev \
    curl build-essential

# Cài đặt Node.js
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# Cài đặt Yarn
sudo npm install -g yarn

# Cài đặt Frappe Bench
sudo pip3 install frappe-bench --break-system-packages
```

#### Bước 3: Khởi Động Services

```bash
# Khởi động MariaDB
sudo service mariadb start

# Khởi động Redis
sudo service redis-server start

# Cấu hình MariaDB (tùy chọn)
sudo mysql_secure_installation
```

#### Bước 4: Khởi Tạo Frappe Bench

```bash
# Tạo thư mục bench
cd ~
bench init frappe-bench --frappe-branch version-15

# Di chuyển vào thư mục bench
cd frappe-bench
```

#### Bước 5: Tạo Site & Cài ERPNext

```bash
# Tạo site mới
bench new-site mysite.localhost --admin-password admin

# Set site làm default
bench use mysite.localhost

# Lấy ERPNext app
bench get-app erpnext

# Cài đặt ERPNext vào site
bench --site mysite.localhost install-app erpnext
```

#### Bước 6: Khởi Động Development Server

```bash
# Khởi động bench
bench start
```

Truy cập: `http://localhost:8000`
- **Username:** Administrator
- **Password:** admin

### Phương Án 2: Kết Nối Database Từ Xa

Nếu bạn có database server riêng:

#### Bước 1: Patch Frappe để hỗ trợ db_user

```bash
# Tải patch script
cd ~/frappe-bench
wget https://raw.githubusercontent.com/[your-repo]/patch_frappe.py

# Chạy patch
python3 patch_frappe.py
```

#### Bước 2: Cấu hình Site Config

Tạo/sửa file `~/frappe-bench/sites/mysite.localhost/site_config.json`:

```json
{
  "db_name": "your_database_name",
  "db_user": "your_db_username",
  "db_password": "your_db_password",
  "db_host": "your_db_host",
  "db_port": 3306,
  "encryption_key": "your_encryption_key"
}
```

#### Bước 3: Cấu hình Common Site Config

Tạo/sửa file `~/frappe-bench/sites/common_site_config.json`:

```json
{
  "db_host": "your_db_host",
  "db_port": 3306,
  "redis_cache": "redis://localhost:6379",
  "redis_queue": "redis://localhost:6379",
  "redis_socketio": "redis://localhost:6379"
}
```

### Phương Án 3: Docker (Khuyến Nghị cho Production)

```bash
# Clone Frappe Docker
git clone https://github.com/frappe/frappe_docker
cd frappe_docker

# Khởi động với Docker Compose
docker compose -f pwd.yml up -d

# Truy cập: http://localhost:8080
# Username: Administrator
# Password: admin
```

---

## 📁 Cấu Trúc Thư Mục

### Cấu Trúc Bench

```
frappe-bench/
├── apps/                      # Các ứng dụng Frappe
│   ├── frappe/               # Frappe Framework core
│   └── erpnext/              # ERPNext application
├── sites/                     # Các site instances
│   ├── assets/               # Compiled assets (JS/CSS)
│   ├── mysite.localhost/     # Site cụ thể
│   │   ├── site_config.json  # Cấu hình site
│   │   ├── private/          # Files riêng tư
│   │   └── public/           # Files công khai
│   └── common_site_config.json
├── config/                    # Cấu hình bench
├── env/                       # Python virtual environment
├── logs/                      # Log files
└── Procfile                   # Process definitions
```

### Cấu Trúc ERPNext App

```
erpnext/
├── erpnext/                   # Module chính
│   ├── accounts/             # Module kế toán
│   │   ├── doctype/          # Định nghĩa DocTypes
│   │   ├── report/           # Báo cáo
│   │   └── page/             # Custom pages
│   ├── stock/                # Module quản lý kho
│   ├── selling/              # Module bán hàng
│   ├── buying/               # Module mua hàng
│   ├── manufacturing/        # Module sản xuất
│   ├── projects/             # Module dự án
│   ├── crm/                  # Module CRM
│   ├── hr/                   # Module nhân sự (nếu có)
│   ├── public/               # Static files (JS/CSS/Images)
│   │   ├── js/               # JavaScript files
│   │   ├── css/              # Stylesheets
│   │   └── images/           # Images
│   ├── templates/            # Jinja2 templates
│   ├── hooks.py              # App hooks & configurations
│   ├── modules.txt           # Danh sách modules
│   └── patches.txt           # Database patches
├── pyproject.toml            # Python dependencies
├── package.json              # Node.js dependencies
└── README.md                 # Documentation
```

### Các File Quan Trọng

| File | Mô Tả |
|------|-------|
| `hooks.py` | Định nghĩa hooks, scheduled jobs, permissions |
| `modules.txt` | Danh sách các module trong app |
| `patches.txt` | Các database migration patches |
| `pyproject.toml` | Python dependencies và build config |
| `package.json` | Frontend dependencies |

---

## 🛠️ Development Workflow

### Cấu Trúc DocType

DocType là đơn vị cơ bản trong Frappe, tương đương với Model trong các framework khác:

```python
# erpnext/accounts/doctype/sales_invoice/sales_invoice.py
from frappe.model.document import Document

class SalesInvoice(Document):
    def validate(self):
        # Business logic validation
        self.calculate_totals()
    
    def on_submit(self):
        # Actions khi submit document
        self.update_stock()
        self.make_gl_entries()
```

### Tạo Module Mới

```bash
# Tạo module mới
bench new-app my_custom_app

# Thêm vào site
bench --site mysite.localhost install-app my_custom_app

# Tạo DocType mới (qua UI hoặc CLI)
bench --site mysite.localhost console
>>> frappe.new_doc("DocType", doctype="My Custom DocType")
```

### Build & Deploy

```bash
# Build assets
bench build --app erpnext

# Clear cache
bench --site mysite.localhost clear-cache

# Migrate database
bench --site mysite.localhost migrate

# Restart services
bench restart
```

### Testing

```bash
# Chạy tests
bench --site mysite.localhost run-tests --app erpnext

# Chạy test cho module cụ thể
bench --site mysite.localhost run-tests --app erpnext --module accounts

# Chạy test cho DocType cụ thể
bench --site mysite.localhost run-tests --doctype "Sales Invoice"
```

---

## 🤝 Đóng Góp & Phát Triển

### Quy Trình Đóng Góp

1. **Fork Repository**
   ```bash
   # Fork trên GitHub, sau đó clone
   git clone https://github.com/your-username/erpnext.git
   cd erpnext
   ```

2. **Tạo Branch Mới**
   ```bash
   git checkout -b feature/ten-tinh-nang-moi
   ```

3. **Phát Triển & Test**
   ```bash
   # Viết code
   # Chạy tests
   bench --site mysite.localhost run-tests --app erpnext
   
   # Kiểm tra code style
   ruff check .
   ```

4. **Commit & Push**
   ```bash
   git add .
   git commit -m "feat: thêm tính năng XYZ"
   git push origin feature/ten-tinh-nang-moi
   ```

5. **Tạo Pull Request**
   - Mở PR trên GitHub
   - Mô tả chi tiết thay đổi
   - Đính kèm screenshots nếu có UI changes

### Coding Standards

**Python:**
- Tuân thủ PEP 8
- Sử dụng type hints khi có thể
- Docstrings cho functions/classes
- Line length: 110 characters

**JavaScript:**
- Sử dụng ES6+ syntax
- Camel case cho variables/functions
- JSDoc comments cho functions

**Git Commit Messages:**
```
feat: thêm tính năng mới
fix: sửa lỗi
docs: cập nhật documentation
style: format code
refactor: tái cấu trúc code
test: thêm/sửa tests
chore: cập nhật dependencies
```

### Tài Liệu Tham Khảo

- **Frappe Framework Docs:** https://frappeframework.com/docs
- **ERPNext User Manual:** https://docs.erpnext.com
- **API Documentation:** https://frappeframework.com/docs/user/en/api
- **Forum:** https://discuss.frappe.io

### Liên Hệ & Hỗ Trợ

- **Maintainer:** Lê Thành Chỉnh
- **Email:** [your-email@example.com]
- **Issues:** https://github.com/frappe/erpnext/issues
- **Discussions:** https://discuss.frappe.io/c/erpnext

---

## 📝 Ghi Chú Quan Trọng

### Troubleshooting

**Lỗi kết nối database:**
```bash
# Kiểm tra MariaDB đang chạy
sudo service mariadb status

# Kiểm tra Redis
sudo service redis-server status

# Xem logs
tail -f ~/frappe-bench/sites/mysite.localhost/logs/web.log
```

**Lỗi permission:**
```bash
# Fix permissions
chmod -R 755 ~/frappe-bench/sites
```

**Clear cache khi gặp lỗi lạ:**
```bash
bench --site mysite.localhost clear-cache
bench restart
```

### Performance Tips

- Sử dụng Redis cache cho production
- Enable query optimization
- Index các fields thường xuyên query
- Sử dụng background jobs cho heavy tasks
- Monitor với Frappe Insights

---

## 📄 License

Dự án này được phân phối dưới giấy phép **GNU General Public License v3.0**.

Copyright © 2025 Lê Thành Chỉnh

---

**Happy Coding! 🚀**
