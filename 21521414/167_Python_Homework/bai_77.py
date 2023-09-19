from math import sqrt

k = int(input("Nhap k: "))
n = int(input("Nhap n: "))

def getPowerOf(a, b):
    temp = 1
    for i in range(1, b + 1):
        temp *= a
    return temp

Sum = 0

for i in range (1, n + 1):
    Sum += getPowerOf(i, k)

print("Sum =", Sum)