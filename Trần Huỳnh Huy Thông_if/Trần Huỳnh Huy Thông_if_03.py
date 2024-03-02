"""Viết chương trình cho người dùng nhập vào một số nguyên n.
Nếu n lẻ thì in ra màn hình dòng chữ “Số lẻ”.
Nếu số n chẵn và lớn hơn hoặc bằng 100 thì in ra màn hình dòng chữ “Số chẵn và lớn hơn hoặc bằng 100”,
ngược lại thì in ra dòng chữ “Số chẵn và bé hơn 100”."""

#Người dùng nhập vào số n;
n = int(input('Nhập số vào đây:'))
print(n)

#Điều kiện nếu số chẵn & lẻ, số chẵn >= 100 & < 100
if (n % 2 != 0):
    print('Số lẻ')
elif (n % 2 == 0 and n >= 100):
    print('Số chẵn và lớn hơn hoặc bằng 100')
else: print('Số chẵn và bé hơn 100')