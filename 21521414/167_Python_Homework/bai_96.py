import math

n = int(input('Nhap n:'))

s = 0
t = 1
i = 1

while i <= n:
    t *= i
    s = math.sqrt(t + s)
    i += 1

print ('s = ', s)
