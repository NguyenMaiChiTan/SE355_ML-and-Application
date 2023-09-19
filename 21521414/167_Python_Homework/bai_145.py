num = abs(int(input("Nhap n: ")))

sqrtN = num**(1/2)

if int(sqrtN) == sqrtN:
    print(f"{num} la so chinh phuong!")
else:
    print(f"{num} khong phai la so chinh phuong!")