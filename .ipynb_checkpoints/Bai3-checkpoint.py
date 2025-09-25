# Nhập dữ liệu
h = int(input("Nhap so gio: "))
m = int(input("Nhap so phut: "))
s = int(input("Nhap so giay: "))

# Chuyển đổi sang tổng số giây
total_seconds = h * 3600 + m * 60 + s

# In kết quả
print(f"Tong so giay cua {h}:{m}:{s} la {total_seconds} giay")
