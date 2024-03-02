#Chương trình tìm số lớn nhất trong 3 số bằng Python:

# Nhap so de tim so lon nhat;
print('Nhap so thu nhat: ')
a= int(input())

print('Nhap so thu hai: ')
b= int(input())

print('Nhap so thu ba: ')
c= int(input())


#Dieu kien de thoa man;
max_number = a
if max_number < b: 
    max_number = b
if max_number < c:
    max_number = c
    print ('So lon nhat la: ', max_number)