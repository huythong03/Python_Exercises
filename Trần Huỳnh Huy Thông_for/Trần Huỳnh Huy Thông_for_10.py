#In ra các số chẵn và số lẻ từ 1 đến 100

#in ra các số chẵn
print("Các số chẵn từ 1 đến 100:")
for i in range(2, 101, 2):
    #vòng lặp có biến thay đổi từ 2 đến 100 (không bao gồm 101), bước nhảy là 2 => i sẽ thay đổi từ 2, 4, 6, 8, ...,98 ,100
    print(i, end=" ")

print("\n")#in ra 1 dòng trống

#in ra các số lẻ
print("Các số lẻ từ 1 đến 100:")
for i in range(1, 101, 2):
    #vòng lặp có biến thay đổi từ 1 đến 100, bước nhảy là 2 => i sẽ thay đổi từ 1, 3, 5, ..., 97, 99
    print(i, end=" ")