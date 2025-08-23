# Nhập thông tin
print("=== TÍNH TIỀN ĐIỆN SINH HOẠT ===")
chi_so_cu = int(input("Nhập chỉ số điện cũ: "))
chi_so_moi = int(input("Nhập chỉ số điện mới: "))

# Tính số điện tiêu thụ
so_dien_tieu_thu = chi_so_moi - chi_so_cu
print("Số điện tiêu thụ trong tháng:", so_dien_tieu_thu, "kWh")

# Tính tiền điện theo bậc thang
tien_dien = 0

if so_dien_tieu_thu <= 100:
    # Bậc 1: 0-100 kWh = 1242 đồng/kWh
    tien_dien = so_dien_tieu_thu * 1242
elif so_dien_tieu_thu <= 150:
    # Bậc 1: 100 kWh đầu = 1242 đồng/kWh
    # Bậc 2: phần còn lại = 1304 đồng/kWh
    tien_dien = 100 * 1242 + (so_dien_tieu_thu - 100) * 1304
elif so_dien_tieu_thu <= 200:
    # Bậc 1: 100 kWh đầu
    # Bậc 2: 50 kWh tiếp
    # Bậc 3: phần còn lại = 1651 đồng/kWh
    tien_dien = 100 * 1242 + 50 * 1304 + (so_dien_tieu_thu - 150) * 1651
elif so_dien_tieu_thu <= 300:
    # Bậc 1: 100 kWh
    # Bậc 2: 50 kWh  
    # Bậc 3: 50 kWh
    # Bậc 4: phần còn lại = 1788 đồng/kWh
    tien_dien = 100 * 1242 + 50 * 1304 + 50 * 1651 + (so_dien_tieu_thu - 200) * 1788
elif so_dien_tieu_thu <= 400:
    # Bậc 1: 100 kWh
    # Bậc 2: 50 kWh
    # Bậc 3: 50 kWh  
    # Bậc 4: 100 kWh
    # Bậc 5: phần còn lại = 1912 đồng/kWh
    tien_dien = 100 * 1242 + 50 * 1304 + 50 * 1651 + 100 * 1788 + (so_dien_tieu_thu - 300) * 1912
else:
    # Trên 400 kWh: bậc cuối = 1962 đồng/kWh
    tien_dien = 100 * 1242 + 50 * 1304 + 50 * 1651 + 100 * 1788 + 100 * 1912 + (so_dien_tieu_thu - 400) * 1962

# Tính thuế VAT 10%
thue_vat = tien_dien * 0.1
tong_tien = tien_dien + thue_vat

# In kết quả
print()
print("=== KẾT QUẢ ===")
print("Tiền điện (chưa VAT):", "{:,.0f}".format(tien_dien), "VNĐ")
print("Thuế VAT (10%):", "{:,.0f}".format(thue_vat), "VNĐ")
print("TỔNG TIỀN PHẢI TRẢ:", "{:,.0f}".format(tong_tien), "VNĐ")