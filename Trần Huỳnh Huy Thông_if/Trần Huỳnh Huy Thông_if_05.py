# Biện luận phương trình bậc hai ax2+bx+c=0.
import math

#Người dùng nhập hệ số
a = float(input('Nhập vào hệ số a: '))
b = float(input('Nhập vào hệ số b: '))
c = float(input('Nhập vào hệ số c: '))

#Điều kiện của phương trình bậc hai
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        print('Phương trình có nghiệm x = ', -c / b)
else: delta = b**2 - 4*a*c
if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print('Phương trình cả hai nghiệm phân biệt: x1 =', x1, 'x2 =', x2)
elif delta == 0:
    print('Phương trình co nghiệm kép: x1 = x2 = ', -b / (2*a))
else: print('Phương trình vô nghiệm')


ket_qua = (a, b, c)
print(ket_qua)
