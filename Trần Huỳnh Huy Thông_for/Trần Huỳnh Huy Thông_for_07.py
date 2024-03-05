#Viết chương trình kiểm tra xem số n có là số nguyên tố hay không
#Số nguyên tố là số chỉ % 1 == 0 && % chính nó == 0

def check_nguyen_to(n):
    if n <= 1: return False
    elif n <= 3: return True
    elif n % 2 == 0 or n % 3 == 0: return False

    #Lặp hàm for kiểm tra số lẻ từ 5 -> căn bậc 2 của n
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0: 
            return False

#Người dùng nhập vào dữ liệu
n = int(input("Nhập vào số nguyên dương:"))
if check_nguyen_to(n): #Kiểm tra số nguyên tố
    print(f"{n} là số nguyên tố")
else: print(f"{n} không phải là só nguyên tố")