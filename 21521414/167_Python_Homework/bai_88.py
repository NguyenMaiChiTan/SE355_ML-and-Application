n = int(input('Nhap n:'))

s = 0
m = 0
i = 1
dau = 1

while i <= n:
    m += i
    s += dau / m
    i += 1
    dau = -dau

print ('s = ', s)
