import math

n = int(input());
s = float(0);
for i in range(1,n+1):
    s+=1/(math.sqrt(i)+math.sqrt(i+1)); 
print(s);