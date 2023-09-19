n = int(input(n))
s = 0
t = 1
i = 1

while i <= n:
    t *= i
    s = (t + s)**(1 / (i + 1))

    i += 1

print ('s = ', s)
