#Tìm ước chung lớn nhất của 2 số nguyên m và n được nhập vào từ bàn phím

def ucln(m,n):
    #So sánh m và n
    while n:
        m, n = n, m % n
    return m
"""vòng lặp while nếu m lớn hơn n thì m trừ đi n
ngược lại nếu n lớn hơn m thì n trừ đi m"""

m = int(input('Nhập vào số nguyên dương m:'))
n = int(input('Nhập vào số nguyên dương n:'))    

#In ra ucln
print(f"Ước chung lớn nhất của {m} và {n} là: {ucln(m, n)}")