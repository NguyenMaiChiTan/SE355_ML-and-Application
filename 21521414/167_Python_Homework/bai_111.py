import math
s = 3
dau = 1
e = 3
i = 2
while(e>10**(-6)):
    e = 4/(i(i+1)*(i+2))
    s = s +dau*e
    i = i + 2
    dau = -dau
   
print(s)