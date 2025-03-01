# Bài 12
# Viết chương trình tính lương của nhân viên dựa theo thâm niên công tác
TNCT = float(input("nhập tháng thâm niên công tác : "))
luong_co_ban = 1350000
if TNCT <12:
    luong = luong_co_ban*2.34
elif 12 <=TNCT<36:
    luong = luong_co_ban*3.33
elif 36 <=TNCT<60:
    luong = luong_co_ban*3.66
else:
    luong = luong_co_ban*3.99
print("Lương của nhận viên là : ", luong ,"đồng")            




