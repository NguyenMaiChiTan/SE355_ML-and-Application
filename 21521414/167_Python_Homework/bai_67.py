from math import sqrt

n = int(input("Nhap n: "))

def findOddNumber(n):
    existOddNumber = False
    if n > 0:
        tempOfn = n;
        while (tempOfn != 0):
            temp = tempOfn % 10
            if (temp % 2) != 0:
                existOddNumber = True
            tempOfn //= 10
    return existOddNumber

if (findOddNumber(n) == True):
    print("Ton tai chu so le trong n")
else:
    print("Khong ton tai chu so le trong n")