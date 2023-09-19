import math

n = int(input());
s = float(0);
for i in range(1,n+1):
    s+=i*(i+1)*(i+2);
print(s);