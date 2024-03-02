# Tính tích các số lẻ (tich = 1x3x5x…x… cho đến khi tich > 50) 

#Tạo biến tích
tich = 1
so_le = 1

#Lặp lại cho đến khi tich > 50
while tich <= 50:
    tich += so_le
    so_le += 2
    
print (f'Tích các số lẻ là: {tich}')