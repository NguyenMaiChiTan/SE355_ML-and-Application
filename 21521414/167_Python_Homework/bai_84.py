from math import sqrt
import math

x = int(input("Nhap x: "))
n = int(input("Nhap n: "))

def getSinOf(x):
    return math.sin(math.radians(x))

Sum = 0

previousValue = x

for i in range (1, n + 1):
    Sum += getSinOf(previousValue);
    previousValue = getSinOf(previousValue)

print("Sum =", Sum)
