from math import sqrt

n = int(input("Nhap n: "))

def findEvenNumber(n):
    existEvenNumber = False;
    if n > 0:
        tempOfn = n;
        while (tempOfn != 0):
            temp = tempOfn % 10
            if (temp % 2) == 0:
                existEvenNumber = True;
            tempOfn //= 10
    elif n == 0:
        existEvenNumber = True;
    else:
        existEvenNumber = False;
    return existEvenNumber;

if (findEvenNumber(n) == True):
    print("Ton tai chu so chan trong n")
else:
    print("Khong ton tai chu so chan trong n")