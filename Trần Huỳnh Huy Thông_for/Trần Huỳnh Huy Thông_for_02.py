#Tính tổng các số lẻ (s = 1+3+5+…+n)

def tong_le(n):
    # dùng list comprehension để tính
    return sum(i for i in range(1, n + 1) if i % 2 != 0)

# xuất ra màn hình
n = int(input("Nhập vào tại đây để tính tổng các số lẻ: "))
ket_qua = tong_le(n)

print(f"Tổng các số lẻ từ 1 đến {n} là: {ket_qua}")