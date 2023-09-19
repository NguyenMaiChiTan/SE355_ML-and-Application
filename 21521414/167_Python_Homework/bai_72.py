from math import sqrt

n = int(input("Nhap n: "))

def calculate(n):
    temp = 0
    for i in range(1, n + 1):
        temp += i
    return 1/temp

Sum = 0

for i in range (1, n + 1):
    Sum += calculate(i)

print("Sum =", Sum)
