import math

n = int(input());
s = int(0);
for i in range(1,n+1):
    if n%i==0:
        if(i%2==0):
            s+=i;
print(s);
