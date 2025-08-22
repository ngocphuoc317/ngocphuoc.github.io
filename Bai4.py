# Nhập dữ liệu
t = int(input("Nhap vao tong so giay: "))

# Tính giờ, phút, giây
h = t // 3600
m = (t % 3600) // 60
s = t % 60

# In kết quả
print(f"{t} giay co dang {h}:{m}:{s}")
