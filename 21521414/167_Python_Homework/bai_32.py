n = int(input())
if (n==0): print('0')
else: 
    res = 0.0
    for i in range(1,n+1):
        res += 1/(i*(i+1))
    print(res)