# bai 1
n = int(input("Nhập số năm: "))
if n % 4 ==0 and n% 100 != 0 or n% 400 ==0:
    print(n, "là năm nhuận")
else:
    print(n, "ko là năm nhuận")    