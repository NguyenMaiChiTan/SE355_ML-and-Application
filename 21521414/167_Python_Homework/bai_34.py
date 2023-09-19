import math
#34-----------------------------------------

n = int(input());
s = float(0);

for i in range(0,n+1):
    s= s+(2*i+1)/(2*i+2);
print(s);