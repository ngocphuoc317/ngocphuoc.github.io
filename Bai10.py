import math

# Nhập tọa độ điểm A
print("Nhập tọa độ điểm A:")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))

# Nhập tọa độ điểm B  
print("Nhập tọa độ điểm B:")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

# Tính khoảng cách
# Công thức: d = √[(x2-x1)² + (y2-y1)²]
khoang_cach = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# In kết quả
print()
print("Điểm A có tọa độ: (", x1, ",", y1, ")")
print("Điểm B có tọa độ: (", x2, ",", y2, ")")
print("Khoảng cách AB =", khoang_cach)