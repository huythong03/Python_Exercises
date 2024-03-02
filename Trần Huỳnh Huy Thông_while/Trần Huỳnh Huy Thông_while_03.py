# Tính tích các số chẵn (tich = 2x4x6x…x… cho đến khi tich > 50) 

#Tạo biến tích
tich = 0
so_chan = 2

#Lặp cho đến khi tích > 50
while tich <= 50:
    tich += so_chan
    so_chan += 2
   
print (f'Tích các só chẵn là: {tich}')
