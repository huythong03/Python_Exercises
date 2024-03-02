#Tính tổng các số chẵn (s = 2+4+6+…+… cho đến khi s>50);

#Tạo biến tổng
s = 0
so_chan = 2

#Lặp cho đến khi > 50
while s + so_chan <= 70: 
    s += so_chan
    so_chan += 2

print (f'Tổng các số chẵn là: {s}')