import math
x = int(input())
xx = (x * 3.14)/180
s = 1
t = 1 
m = 1
dau = 1
e = 1
i = 1
while(e>10**(-6)):
    t = t *x
    m = m * i
    e = t/m
    s = s +e
    i = i + 1
   
print(s)