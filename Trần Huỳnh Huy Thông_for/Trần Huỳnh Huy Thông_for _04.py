#Tính tích các số lẻ (tich = 1x3x5x…x n)

def tich_le(n):
    tich = 1
    for i in range(1, n + 1, 2): #Lặp từ 2 dến n bước nhảy là 1
        tich *= i #Mỗi vòng lặp * i
    return tich

n = int(input("Nhập vào tại đây để tính tích các số lẻ:"))
ket_qua = tich_le(n)

print(f"Tích cá số lẻ từ 1 đến {n} là: {ket_qua}")