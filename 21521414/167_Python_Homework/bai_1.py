import math
x1,y1= map(int, input('Nhap toa do diem thu 1: \n x1, y1: ').split())
x2,y2= map(int, input('Nhap toa do diem thu 2: \n x2, y2: ').split())
d = math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
print('Khoang cach',d)
