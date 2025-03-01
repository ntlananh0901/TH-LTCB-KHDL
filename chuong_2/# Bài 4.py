# Bài 4
a = float(input("nhập số a: "))
b = float(input("nhập số b: "))
c = float(input("nhập số c: "))
if a > b and a> c:
    so_lon_nhat = a
elif b>a and b>c:
    so_lon_nhat = b
else:
    so_lon_nhat = c
print("số lớn nhất là :", so_lon_nhat)