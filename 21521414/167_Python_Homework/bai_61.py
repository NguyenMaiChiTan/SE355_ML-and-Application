n = int(input())
res = 0
while (n>0):
    if((n%10)%2!=0):
        res += 1
    n = n//10
print(res)