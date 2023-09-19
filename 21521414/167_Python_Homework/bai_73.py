from math import sqrt

x = int(input("Nhap x: "))
n = int(input("Nhap n: "))

def calculate(x, n):
    numerator = 1
    denominator = 0
    for i in range(1, n + 1):
        numerator *= x
        denominator += i
    return numerator/denominator

Sum = 0

for i in range (1, n + 1):
    Sum += calculate(x, i)

print("Sum =", Sum)

