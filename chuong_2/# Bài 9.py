# Bài 9
#viết chương trình nhập lương nhan viên, tính thuế thu nhập và lương ròng
luong = int(input("Nhập lương của bạn: "))
if luong == 15 :
    luong_rong = luong*0.3
elif 7<= luong< 15:
    luong_rong = luong*0.2
else:
    luong_rong = luong*0.1
luong_nhan_dc = luong - luong_rong
print("lương thực sự mà nhân viên đó nhận dc là:", luong_nhan_dc, "triệu đồng") 
       