x = int(input('Nhap x:'))
n = int(input('Nhap n:'))

s = 0
t = 1
i = 1

dau = 1

while (i <= n):
    t *= x
    s += dau * t
    i += 1
    dau = -dau

print ('s = ', s)
