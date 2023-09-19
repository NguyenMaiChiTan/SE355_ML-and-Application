from math import sqrt
import math

x = int(input("Nhap x: "))
n = int(input("Nhap n: "))

def getPowerOf(a, b):
    temp = 1
    for i in range(1, b + 1):
        temp *= a
    return temp

Sum = 0

for i in range (1, n + 1):
    Sum += math.sin(math.radians(getPowerOf(x, i)))

print("Sum =", Sum)

