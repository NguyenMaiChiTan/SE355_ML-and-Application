import math
s = 1
m = 1
e = 1
i = 1
while(e>10**(-6)):
    m = m * i
    e = 1/m
    s = s +e
    i = i + 1
   
print(s)