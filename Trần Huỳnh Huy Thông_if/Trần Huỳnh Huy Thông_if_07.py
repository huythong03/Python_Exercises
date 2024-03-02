"""
Hãy nhập vào tuổi của một người và đưa ra kết luận là lứa tuổi của người đó theo quy tắc sau:
*tuổi > 0 và <= 2 là trẻ sơ sinh
*tuổi > 2 và <= 10 là nhi đồng
*tuổi > 10 và <= 17 là vị thành niên
*tuổi > 17 và <= 39 là thanh niên
*tuổi > 39 và <= 50 là trung niên
*tuổi > 50 là cao niên
"""

#Nhập số tuổi của người dùng;
tuoi = int(input('Nhập vào số tuổi của bạn:'))

#kết luận lứa tuổi của người dùng;
if (tuoi > 0 and tuoi <= 2): print('Bạn là trẻ sơ sinh')
if (tuoi > 2 and tuoi <= 10): print('Bạn là nhi đồng')
if (tuoi > 10 and tuoi <= 17): print('Bạn là vị thành niên')
if (tuoi > 17 and tuoi <= 39): print('Bạn là thanh niên')
if (tuoi > 39 and tuoi <= 50): print('Bạn là trung niên')
if (tuoi > 50): print('Bạn là cao niên')