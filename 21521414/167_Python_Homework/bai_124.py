import math
n = int(input())
i = 2
at = 2
bt = 1
while(i<=n):
    ahh = 2*bt*bt +at*at
    bhh = at*2*bt
    i = i +1
    at = ahh
    bt =bhh
print(ahh)