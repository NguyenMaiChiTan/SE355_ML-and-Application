import math

x = float(input("input x: "));
n = int(input("input n: "));
q= float(1);
for i in range(1,n+1):
    q*=x;
print(q);