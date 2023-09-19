x = int(input('Nhap x:'))
n = int(input('Nhap n:'))

s = 1 - x
t = x
m = 1
i = 3
dau = 1

while i <= 2 * n + 1:
    t *= x * x
    m *= i * (i - 1)
    s += dau * t / m
    i += 2
    dau = -dau

print ('s = ' s)
