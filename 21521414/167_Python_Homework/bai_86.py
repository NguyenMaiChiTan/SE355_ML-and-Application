x = int(input('Nhap x:'))
n = int(input('Nhap n:'))

s = 0
t = 1
i = 2

dau = -1

while (i <= 2 * n):
    t *= x * x
    s += dau * t
    i += 2
    dau = -dau

print ('s = ', s)
