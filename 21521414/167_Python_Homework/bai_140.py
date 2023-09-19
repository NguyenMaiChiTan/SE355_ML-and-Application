a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

delta = b**2 - 4*a*c

if delta<=0:
    if delta==0:
        print(-b/(2*a))
    else:
        print("Vo nghiem!")
else:
    x1 = (-b + delta**(1/2))/(2*a)
    x2 = (-b - delta**(1/2))/(2*a)
    print(x1, x2)