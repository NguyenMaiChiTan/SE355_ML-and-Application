x = int(input('Nhap x:'))
n = int(input('Nhap n:'))

s = -1
t = 1
m = 1
i = 2
dau = 1

while i <= 2 * n:
    t *= x * x
    m *= i * (i - 1)
    s += dau * t / m
    i += 2
    dau = -dau

print ('s = ' s)
