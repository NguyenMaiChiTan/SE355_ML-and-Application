import math

n = int(input("input n:"));
x = int(input("input x:"));
s = float(1);
for i in range(0,n+1):
    s*=(x+i);
print(s);