import math
s = 0
dau = 1
e = 4
i = 1
while(e>10**(-6)):
    e = 4/i
    s = s +dau*e
    i = i + 2
    dau = -dau
   
print(s)