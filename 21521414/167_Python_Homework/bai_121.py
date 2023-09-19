import math
n = int(input())
i = 2
at = 1
att =1
while(i<=n):
    ahh = at + att
    i = i +1
    att = at
    at = ahh
print(ahh)