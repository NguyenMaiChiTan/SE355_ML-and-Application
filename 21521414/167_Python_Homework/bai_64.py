from math import sqrt

n = int(input("Nhap n: "))

if n > 0:
    maxNumber = n % 10;

    tempOfn = n;

    while (tempOfn != 0):
        temp = tempOfn % 10
        if temp > maxNumber:
            maxNumber = temp
        tempOfn //= 10

    print("Chu so lon nhat trong so nguyen duong", n, "la", maxNumber);
else:
    print("n khong hop le.")