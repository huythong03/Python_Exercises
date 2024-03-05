#Tính tích các số chẵn (tich = 2x4x6x…x n)

def tich_chan(n):
    tich = 1
    for i in range(2, n + 1, 2): #Lặp từ 2 dến n bước nhảy là 2
        tich *= i #Mỗi vòng lặp * i
    return tich

n = int(input("Nhập vào tại đây để tính tích các số chẵn: "))
ket_qua = tich_chan(n)

print(f"Tích các số chẵn từ 1 đến {n} là: {ket_qua}")