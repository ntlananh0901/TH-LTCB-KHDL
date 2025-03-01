# Bài 10
x = int(input("Nhập số tháng: "))
if x == 2:
    n = int(input("Nhập số năm: "))
    if n % 4 ==0 and n% 100 != 0 or n% 400 ==0:
        print(n, "là năm nhuận")
        print("tháng 2 có 29 ngày")
    else:
        print(n, "ko là năm nhuận") 
        print("tháng 2 có 28 ngày")  
else:
    if x % 2 == 0:
        print("tháng", x, "có  30 ngày")
    else:
        print("tháng", x, "có 31 ngày")
            