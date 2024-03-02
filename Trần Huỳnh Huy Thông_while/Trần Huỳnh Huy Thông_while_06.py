"""
Nhập vào số nguyên dương n
Kiểm tra số n có phải là số nguyên tố không
"""

#Nhập số n;
n = int(input('Nhập số nguyên dương n: '))

if n == 1 or n == 2: print(n,'là số nguyên tố')
elif n % 2 == 0: print(n,'không phải là số nguyên tố')
else: flag = True #if n là số nguyên tố

#Khởi tạo biến
i = 2
#Duyệt các số lẻ từ 2 đến các bậc 2 của n

while i <= n**0.5:
    if n % i == 0:
        flag = False
        break
    i += 1

if flag:
   print(n,'là số nguyên tố')
else: print(n,'không phải là số nguyên tố')