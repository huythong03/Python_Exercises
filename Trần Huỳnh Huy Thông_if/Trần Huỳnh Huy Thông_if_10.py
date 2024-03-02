"""
*Nhập số N bất kỳ từ bàn phím
*N có phải số nguyên không?
*Kiểm tra tính chẵn lẻ của N
*N có phải là số chẵn dương không?
*N có phải là số lẻ âm không?
*N có phải số chính phương không?
"""

#Nhập số bất kỳ
n = float(input('Nhập số N bất kỳ:'))

#Kiểm tra N có phải là số nguyên không?;
if n.is_integer(): print(n,' là số nguyên')
else: print(n,' không phải là số nguyên')

#Kiểm tra tính chẵn lẻ của N;
if (n % 2 == 0): print(n,' là số chẵn')
else: print(n,' là số lẻ')

#N có phải là số chẵn dương không?;
if (n > 0 and n % 2 == 0): print(n,' là số chẵn dương')
else: print(n,' không phải là số chẵn dương')

#N có phải là số lẻ âm không?;
if(n < 0 and n % 2 != 0): print(n,' là số lẻ âm')
else: print(n,' không phải là số lẻ âm')

#N có phải là số chính phương không?;
if (n >= 0 and int(n ** 0.5) **2 == n): print(n,' là số chính phương')
else: print(n,' không phải là số chính phương')