# Tính tổng các số lẻ (s = 1+3+5+…+… cho đến khi s>50);

#Tạo biến tổng
s = 0
so_le = 1

#Lặp cho đến khi s > 50
while s + so_le < 70:
    s += so_le
    so_le += 2

print (f'Tổng các số lẻ là: {s}')