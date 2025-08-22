import math

# Nhập độ dài 3 cạnh
a = float(input("Nhap do dai canh a: "))
b = float(input("Nhap do dai canh b: "))
c = float(input("Nhap do dai canh c: "))

# Nửa chu vi
p = (a + b + c) / 2

# Công thức Heron
S = math.sqrt(p * (p - a) * (p - b) * (p - c))

# In kết quả với 2 số lẻ thập phân
print(f"Dien tich tam giac S = {S:.2f}")
