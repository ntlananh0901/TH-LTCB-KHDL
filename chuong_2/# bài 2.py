# bài 2
import math
x  = int(input("Nhập x: "))
y  = int(input("Nhập y: "))
a  = int(input("Nhập a: "))
b  = int(input("Nhập b: "))
r  = int(input("Nhập r: "))
IM = math.sqrt((x-a)**2 + (y-b)** 2)
print("IM =", IM)
if IM > r:
    print("điểm M nằm ngoài đường tròn")
elif IM <= r:
    print("Điểm M nằm trong đường tròn") 

