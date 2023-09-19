from math import sqrt

def getFactorial(x):
    temp = 1
    for i in range(1, x + 1):
        temp *= i
    return temp

n = int(input("Nhap n: "))
Sum = 0

for i in range(1, n + 1):
    Sum += getFactorial(i)

print("S(n) =", Sum)