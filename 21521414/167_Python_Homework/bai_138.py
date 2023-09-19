x = float(input("Nhap x: "))

if x>=0:
    if x<=1:
        print(5*x - 7)
    else:
        print(2*x**3 + 5*x**2 - 8*x + 3)
else:
    print(-2*x**3 + 6*x + 9)