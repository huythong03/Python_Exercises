#Chương trình in ra các ngày trong tháng bằng Python:

#in ra các ngày trong tháng;
print('Nhap so thang: ')
thang=int(input())


#điều kiện các ngày trong tháng;
if thang in [1, 3, 5, 7, 8, 10, 12]:
    so_ngay = 31
elif thang in [4, 6, 9, 11]:
    so_ngay = 30
else: 
    so_ngay = 28

print(f"Thang {thang} co {so_ngay} ngay: ")