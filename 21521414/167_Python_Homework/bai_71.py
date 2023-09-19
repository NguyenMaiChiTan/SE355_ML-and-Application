from math import sqrt

x = int(input("Nhap x: "))
n = int(input("Nhap n: "))

def getPowerOf(a, b):
    temp = 1
    for i in range(1, b + 1):
        temp *= a
    return temp

Sum = 0

for i in range (0, n + 1):
    Sum += getPowerOf(x, i * 2 + 1)

print("Sum =", Sum)