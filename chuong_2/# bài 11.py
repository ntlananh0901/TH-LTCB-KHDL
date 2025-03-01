# bài 11
def doc_so(so):
    hang_tram = so // 100
    hang_chuc = (so % 100) // 10
    hang_don_vi = so % 10
    
    doc_so_hang = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    
    ket_qua = doc_so_hang[hang_tram] + " trăm "
    
    if hang_chuc == 0 and hang_don_vi != 0:
        ket_qua += "linh "
    elif hang_chuc != 0:
        if hang_chuc == 1:
            ket_qua += "mười "
        else:
            ket_qua += doc_so_hang[hang_chuc] + " mươi "
    
    if hang_don_vi != 0:
        ket_qua += doc_so_hang[hang_don_vi]
    
    return ket_qua

# Ví dụ
so = int(input("Nhập số nguyên có ba chữ số: "))
print("Cách đọc: " + doc_so(so))
