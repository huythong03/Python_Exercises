"""
Nhập số nguyên n. Viết chương trình để tạo ra một dãy số chứa (i : i*i) như là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dãy số này.
Ví dụ: số n là 8 thì đầu ra sẽ là:
1: 1   2: 4   3: 9   4: 16   5: 25    6: 36    7: 49   8: 64
"""

def day_so(n):
    for i in range(1, n + 1):
        print(f"{i}: {i * i}")

n = int(input("Nhập n:"))
day_so(n)