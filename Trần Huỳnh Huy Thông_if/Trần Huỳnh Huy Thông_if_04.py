# Biện luận phương trình bậc nhất ax+b=0.

#Người dùng nhập hệ số
a = float(input('Nhập vào hệ số a:'))
b = float(input('Nhập vào hệ số b:'))

#Điều kiện của phương trình bậc nhất
if a != 0:
    x = -b / a
    print (f"Phương trình có nghiệm duy nhất: x = {x}")
elif b == 0:
    print( "Phương trình có tập nghiệm là R (tất cả các số thực)")
else:
    print( "Phương trình vô nghiệm")