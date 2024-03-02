#Viết chương trình Python phân tích số nguyên n thành các thừa số nguyên tố. Ví dụ: 12 = 2 x 2 x 3.

def phan_tich_thua_so_nguyen_to(n):
#Nhận vào số nguyên dương n và trả về danh sách các thừa số nguyên tố n
    thua_so_nguyen_to = []
    i = 2 
    #Lặp qua các số từ 2 đến n, kiểm tra xem số nào là ước số của n
    while i <= n:
        if n % i == 0:
            thua_so_nguyen_to.append(i)
        #Nếu 1 số là ước số của n thì sẽ thêm vào danh sách các thừa số nguyên tố
        while n % i == 0:
            #Chia cho n cho đến khi không chia hết cho số đó
            n //= i
        i += 1
    #Sau khi lặp qua tất cả các số từ 2 đến n. Trả về danh sách các thừa số nguyên tố n
    return thua_so_nguyen_to

n = int(input("Nhập vào số nguyên dương n: "))
thua_so_nguyen_to = phan_tich_thua_so_nguyen_to(n)
print(f"Phân tích số {n} thành các thừa số nguyên tố: {thua_so_nguyen_to}")
