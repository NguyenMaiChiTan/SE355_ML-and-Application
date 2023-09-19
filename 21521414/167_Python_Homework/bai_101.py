s = 0
e = 1
i = 1

bound = 10**-6

while e >= bound:
    e = 1 / i
    s += e
    i += 1

rounded_s = round(s, 6)

print ('s = ', rounded_s)
