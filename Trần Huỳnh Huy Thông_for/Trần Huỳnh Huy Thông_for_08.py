"""
Viết chương trình tính tổng của các chữ số của môt số nguyên dương n trong Python.
Số nguyên dương n được nhập từ bàn phím
"""

def sum_chu_so(n):
    tong = 0
    #Chuyển n thành chuỗi
    chuoi_n = str(n)
    #Duyệt qua từng ký tự trong chuỗi
    for chu_so in chuoi_n: 
        #Cộng gái trị ASCII của ký tự vào tổng
        tong += ord(chu_so) - ord('0')
    return tong

#Nhập số nguyên dương n từ người dùng
n = int(input("Nhập vào số nguyên dương n:"))

#Tính tổng các chữ số n
ket_qua = sum_chu_so(n)

#In ra màn hình
print(f"Tổng các chữ só của {n} là: {ket_qua}")