# Nhập ngày, tháng, năm
print("=== TÌM NGÀY TRƯỚC ĐÓ ===")
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Hàm kiểm tra năm nhuận
def kiem_tra_nam_nhuan(nam):
    if nam % 4 == 0:
        if nam % 100 == 0:
            if nam % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Hàm tìm số ngày của tháng
def so_ngay_cua_thang(thang, nam):
    if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
        return 31
    elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
        return 30
    elif thang == 2:
        if kiem_tra_nam_nhuan(nam):
            return 29
        else:
            return 28

# Tìm ngày trước đó
if ngay == 1:
    # Nếu là ngày đầu tháng
    if thang == 1:
        # Nếu là ngày đầu năm
        ngay_truoc = 31
        thang_truoc = 12
        nam_truoc = nam - 1
    else:
        # Không phải ngày đầu năm
        thang_truoc = thang - 1
        nam_truoc = nam
        ngay_truoc = so_ngay_cua_thang(thang_truoc, nam_truoc)
else:
    # Không phải ngày đầu tháng
    ngay_truoc = ngay - 1
    thang_truoc = thang
    nam_truoc = nam

# In kết quả
print()
print("Ngày hiện tại:", str(ngay) + "/" + str(thang) + "/" + str(nam))
print("Ngày trước đó:", str(ngay_truoc) + "/" + str(thang_truoc) + "/" + str(nam_truoc))