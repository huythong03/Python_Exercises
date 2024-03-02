"""
Hãy nhập vào 1 điểm trung bình và xét học bổng đối với điểm trung bình đó theo quy tắc sau: 

*Nếu điểm trung bình >= 9 thì học bổng là 5m
*Nếu điểm trung bình >= 8 và < 9 thì học bổng là 3m
*Nếu điểm trung bình >= 7 và < 8 thì học bổng là 1m
*Những trường hợp còn lại học bổng = 0
"""

#Nhập vào điểm trung bình;
diem_tb = int(input('Nhập vào điểm trung bình:'))

#Xét học bổng đối với điểm trung bình;
if (diem_tb >= 9): print('Chúc mừng! Bạn nhận được học bổng 5.000.000')
elif (diem_tb >= 8 and diem_tb < 9): print('Chúc mừng! Bạn nhận đưuọc học bổng là 3.000.000')
elif (diem_tb >= 7 and diem_tb < 8): print('Chúc mừng! Bạn nhận được học bổng là 1.000.000')
else: print('Xin lỗi! Bạn không nhận được học bổng nào hết!')