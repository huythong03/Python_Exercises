#Tính n! (n giai thừa) 

def tinh_gia_thua(n):
    giai_thua = 1 
    for i in range(1, n + 1):
        giai_thua *= i
    return giai_thua

n = int(input("Nhập vào giai thừa: "))
ket_qua = tinh_gia_thua(n)

print(f"Giai thừa của {n} là: {ket_qua}")