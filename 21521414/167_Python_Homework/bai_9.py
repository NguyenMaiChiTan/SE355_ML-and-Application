import math
n = int(input('Nhap so canh cua da giac: '))
r = float(input('Nhap ban kinh duong tron: '))
S = 1/2*n*pow(r,2)*math.sin(2*3.14/n)
print('Dien tich cua da giac deu n canh noi tiep trong duong tron: ',S)
