As = list(map(float, input("Nhap Xa, Ya: ").split()))
Bs = list(map(float, input("Nhap Xb, Yb: ").split()))
Cs = list(map(float, input("Nhap Xc, Yc: ").split()))

a = ((As[0]-Bs[0])**2 + (As[1]-Bs[1])**2)**(1/2)
b = ((Cs[0]-Bs[0])**2 + (Cs[1]-Bs[1])**2)**(1/2)
c = ((As[0]-Cs[0])**2 + (As[1]-Cs[1])**2)**(1/2)

if a+b>c and a+c>b and b+c>a:
    print("La tam giac!")
else:
    print("Khong la tam giac!")