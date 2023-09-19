from math import sqrt

x = int(input("Nhap x: "))
n = int(input("Nhap n: "))

def getFactorial(x):
    temp = 1
    for i in range(1, x + 1):
        temp *= i
    return temp

def calculate(x, n):
    numerator = 1
    denominator = getFactorial(n)
    for i in range(1, n + 1):
        numerator *= x
    return numerator/denominator

Sum = 0

for i in range (1, n + 1):
    Sum += calculate(x, i)

print("Sum =", Sum)

