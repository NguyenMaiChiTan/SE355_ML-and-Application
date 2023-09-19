n = int(input())
res = 1
while (n>0):
    temp = n%10
    if(temp%2!=0):
        res *= temp
    n = n//10
print(res)