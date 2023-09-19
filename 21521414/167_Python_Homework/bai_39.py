import math

n = int(input());
s = float(1);
for i in range(1,n+1):
    s*=(1+1/(i**2));
print(s);