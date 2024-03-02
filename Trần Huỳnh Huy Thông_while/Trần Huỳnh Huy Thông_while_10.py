# Viết chương trình tính tổng các chữ số của một số nguyên n. Ví dụ: 1234 = 1 + 2 + 3 + 4 = 10.

n = int(input('Nhập vào số nguyên n:'))
tong = 0 #Biến tổng lưu trữ các chữ số 

#Lấy từng chữ số của 'n' + vào trong 'tong'
while n > 0:
    tong += n % 10 #Lấy chữ số cuối cùng
    n //= 10 #Loại bỏ chữ số cuối cùng

print('Tổng các chữ số của một số nguyên n là: ', tong)