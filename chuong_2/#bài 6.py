#bài 6
print("---MENU---")
print("Chào mừng đến với rạp chiếu phim ABC!")
print("mời bạn chọn loại phim muốn xem")
print("1. Phim hành động")
print("2. Phim tình cảm ")
print("3. Phim khoa học viễn tưởng")
print("4. Phim kinh dị")
a = input("Chọn loại phim muốn xem:")
if a == "1":
    print("Bạn đã chọn phim hành động")
elif a == "2":
    print("Bạn đã chọn phim tình cảm")
elif a == "3":
    print("Bạn đã chọn phim khoa học viễn tưởng")
elif a == "4":
    print("Bạn đã chọn phim kinh dị")
else:    
    print("ko có loại phim này")