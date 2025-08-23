# Nhập 2 số
print("=== MÁY TÍNH ĐƠN GIẢN ===")
so_thu_nhat = float(input("Nhập số thứ nhất: "))
so_thu_hai = float(input("Nhập số thứ hai: "))

# Nhập phép toán
print("\nCác phép toán có thể làm:")
print("+ : Phép cộng")
print("- : Phép trừ") 
print("* : Phép nhân")
print("/ : Phép chia")

phep_toan = input("\nNhập phép toán (+, -, *, /): ")

# Tính toán và hiển thị kết quả
print("\nKết quả:")
if phep_toan == "+":
    ket_qua = so_thu_nhat + so_thu_hai
    print(so_thu_nhat, "+", so_thu_hai, "=", ket_qua)
    
elif phep_toan == "-":
    ket_qua = so_thu_nhat - so_thu_hai
    print(so_thu_nhat, "-", so_thu_hai, "=", ket_qua)
    
elif phep_toan == "*":
    ket_qua = so_thu_nhat * so_thu_hai
    print(so_thu_nhat, "*", so_thu_hai, "=", ket_qua)
    
elif phep_toan == "/":
    if so_thu_hai == 0:
        print("Không thể chia cho 0!")
    else:
        ket_qua = so_thu_nhat / so_thu_hai
        print(so_thu_nhat, "/", so_thu_hai, "=", ket_qua)
        
else:
    print("Phép toán không hợp lệ!")

print("\n=== HẾT ===")
