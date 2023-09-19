num = abs(int(input("Nhap n: ")))

num = str(num)
revNum = num[::-1]
if num==revNum:
    print(f"{num} la so doi xung!")
else:
    print(f"{num} khong phai la so doi xung!")