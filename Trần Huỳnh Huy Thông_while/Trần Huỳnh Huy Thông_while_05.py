"""
Tìm bội chung nhỏ nhất của 2 số nguyên m và n được nhập vào từ bàn phím.
(Bội chung nhỏ nhất của 2 số là 1 số nhỏ nhất mà nó chia hết cho 2 số đó,
ví dụ: BCNN(6,4)=12, BCNN(3,10)=30
"""

#BCNN
m = int(input('Nhập vào bội số chung:'))
n = int(input('Nhập vào bội số chung:'))
tich = m * n

while m != n: 
    if m > n:
        m -= n
    else: 
        n -= m

print (f"Bội chung nhỏ nhất là: {tich // m}")