"""Người dùng nhập vào một năm là một số nguyên dương bất kì. 
Cho biết năm đó có là năm nhuận hay không?"""

#Người dùng nhập vào số năm dương bất kì;
nam = int(input('Nhập vào số năm:'))

#Kiểm tra xem năm đó có là năm nhận hay không;
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print(f"{nam} là năm nhuận.")
else:
        print(f"{nam} không phải là năm nhuận.")
