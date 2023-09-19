s = 0
m = 0
e = 1
i = 1

bound = 10**-6
while e >= bound:
    m += i
    e = 1 / m
    s += e
    i += 1

rounded_s = round(s, 6)
print ('s = ', rounded_s)
