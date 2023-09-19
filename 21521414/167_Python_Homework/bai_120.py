import math
n = int(input())
i = 2
at = 2
while(i<=n):
    ahh = 5*at + math.sqrt(24*at*at-8)
    i = i +1
    at = ahh
print(ahh)