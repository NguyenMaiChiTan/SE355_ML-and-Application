from math import sqrt

n = int(input("Nhap n: "))

def getFactorial(x):
    temp = 1
    for i in range(1, x + 1):
        temp *= i
    return temp

Sum = 0

for i in range (1, n + 1):
    Sum += i * getFactorial(i)

print("Sum =", Sum)