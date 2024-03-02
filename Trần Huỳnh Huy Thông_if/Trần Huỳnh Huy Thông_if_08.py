"""
Hãy nhập vào năm sản xuất của một chiếc máy tính,
sau đó đưa ra đề xuất đối với máy tính đó theo quy tắc sau:

*Nếu năm sản xuất >= 15 thì đưa ra đề xuát 'Thay the
*Nếu năm sản xuất >= 10 thì đưa ra đề xuất 'Bao tri
*Những trường hợp khác đưa ra đề xuất 'Khong co de xuat
"""

#Nhập vào năm sản xuất của một chiếc máy tính;
nam_sx = int(input())

if (nam_sx >= 15): print('Thay the')
elif (nam_sx >= 10): print('Bao tri')
else: print('Khong co de xuat')