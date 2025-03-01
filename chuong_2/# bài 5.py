# bài 5
ki_tu = input("Nhập kí tự: ")
nguyen_am = "aeiouAEIOU"
if ki_tu in nguyen_am:
    print( ki_tu, "là nguyên âm")
else:
    print(ki_tu,"là phụ âm")