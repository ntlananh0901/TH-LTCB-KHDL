# BÀi 3
a = int(input("Nhập cạnh a:"))
b = int(input("Nhập cạnh b:"))
c = int(input("Nhập cạnh c:"))
if a + b >c and a + c > b and b + c > a:
    print("đây là tam giác")
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("đây là tam giác vuong")
    elif a**2 +b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Đây là tam giác vuông cân")
    elif a==b  or a==c or b ==c:
        print("đây là tam giác cân")
    elif a==b==c:
        print("Đây là tam giác đều")    
else:
    print("đây ko là tam giác")