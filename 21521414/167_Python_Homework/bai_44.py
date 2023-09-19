import math

n = int(input());
s = float(0);
for i in range(1,n+1):
    s+=1/(i*(i+1)*(i+2)*(i+3));
print(s);