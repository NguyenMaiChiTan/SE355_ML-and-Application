import math

n = int(input('Nhap n:'))

s = 0
i = n

while i > 0:
    s = math.sqrt(i + s)
    i -= 1

print ('s = ', s)
