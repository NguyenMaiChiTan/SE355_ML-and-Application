import math

n = int(input());
s = int(0);
for i in range(1,n+1):
    s+=i**3;
print(s);