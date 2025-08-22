# Nhập số nguyên có 4 chữ số
x = int(input("Nhap so nguyen co 4 chu so: "))

# Tách các chữ số
d1 = x // 1000            # chữ số hàng nghìn
d2 = (x // 100) % 10      # chữ số hàng trăm
d3 = (x // 10) % 10       # chữ số hàng chục
d4 = x % 10               # chữ số hàng đơn vị

# Đảo số
y = d4 * 1000 + d3 * 100 + d2 * 10 + d1

# In kết quả
print(f"So dao cua {x} la {y}")
