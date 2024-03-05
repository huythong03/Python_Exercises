#Viết chương trình in ra bảng cửu chương bằng vòng lặp for.

for i in range(1, 10): #lặp từ 1 đến 9 (không bao gồm 10)
    print(f"Bảng cửu chương {i}: ")
    for j in range(1, 10): #Giống vòng lặp for đầu tiên
        print(f"{i} x {j} = {i * j}") #in ra phép nhân và kết quả của phép nhân trong bảng cửu chương