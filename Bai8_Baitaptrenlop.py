# Nhập 3 cạnh của tam giác
print("=== KIỂM TRA TAM GIÁC ===")
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra điều kiện tạo thành tam giác
# Điều kiện: a + b > c và a + c > b và b + c > a
if a + b > c and a + c > b and b + c > a:
    print("a, b, c có thể tạo thành một tam giác")
    
    # Tìm cạnh lớn nhất
    if a >= b and a >= c:
        canh_lon_nhat = a
        print("Cạnh lớn nhất là a =", canh_lon_nhat)
    elif b >= a and b >= c:
        canh_lon_nhat = b
        print("Cạnh lớn nhất là b =", canh_lon_nhat)
    else:
        canh_lon_nhat = c
        print("Cạnh lớn nhất là c =", canh_lon_nhat)
        
    print("Max(" + str(a) + ", " + str(b) + ", " + str(c) + ") = " + str(canh_lon_nhat))
    
else:
    print("a, b, c KHÔNG thể tạo thành tam giác")
    
    # Vẫn tìm số lớn nhất
    if a >= b and a >= c:
        so_lon_nhat = a
    elif b >= a and b >= c:
        so_lon_nhat = b
    else:
        so_lon_nhat = c
        
    print("Số lớn nhất trong 3 số là:", so_lon_nhat)