s = 0
e = 0.5
i = 2

bound = 10**-6

while e >= bound:
    e = 1 / i
    s += e
    i += 2

rounded_s = round(s, 6)
print ('s = ', rounded_s)