import math
n = int(input())
i = 2
at = 2
bt = 1
while(i<=n):
    ahh = 3*bt +2*at
    bhh = at + 3*bt
    i = i +1
    at = ahh
    bt =bhh
print(ahh)