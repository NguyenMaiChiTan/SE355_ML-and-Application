n = int(input())
res = 0
while (n>0):
    temp = n%10
    if(temp%2==0):
        res += temp
    n = n//10
print(res)