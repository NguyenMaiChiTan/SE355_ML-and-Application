x = int(input('Nhap x:'))
n = int(input('Nhap n:'))

s = x
t = x
i = 3

dau = -1

while (i <= 2 * n + 1):
    t *= x * x
    s += dau * t
    i += 2
    dau = -dau

print ('s = ', s)
