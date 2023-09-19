import math
x1,y1 = map(int, input('Nhap toa do diem A: \n x1, y1: ').split())
x2,y2 = map(int, input('Nhap toa do diem B: \n x2, y2: ').split())
x3,y3 = map(int, input('Nhap toa do diem C: \n x3, y3: ').split())
a=math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
b=math.sqrt(pow(x3-x2,2)+pow(y3-y2,2))
c=math.sqrt(pow(x1-x3,2)+pow(y1-y3,2))
P = a+b+c
n = P/2
S = math.sqrt(n*(n-a)*(n-b)*(n-c))
print('Dien tich cua tam giac: ',S)