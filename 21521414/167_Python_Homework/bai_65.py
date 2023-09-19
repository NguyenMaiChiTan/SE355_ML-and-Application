from math import sqrt

n = int(input("Nhap n: "))

if n > 0:
    minNumber = n % 10;

    tempOfn = n;

    while (tempOfn != 0):
        temp = tempOfn % 10
        if temp < minNumber:
            minNumber = temp
        tempOfn //= 10

    print("Chu so nho nhat cua so nguyen duong", n, "la", minNumber);
else:
    print("n khong hop le.")