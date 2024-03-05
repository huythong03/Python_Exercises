#Tính tổng các số chẵn (s = 2+4+6+…+n)

def tong_chan(n):
    # dùng list comprehension để tính
    return sum(i for i in range(1, n + 1) if i % 2 == 0)

# xuất ra màn hình
n = int(input("Nhập vào tại đây để tính tổng các số chẵn: "))
ket_qua = tong_chan(n)

print(f"Tổng các số chẵn từ 1 đến {n} là: {ket_qua}")