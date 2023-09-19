import math

n = int(input('Nhap n:'))

s = 0
i = 1

while i <= n:
    s = math.sqrt(2 + s)
    i += 1

print ('s = ', s)
