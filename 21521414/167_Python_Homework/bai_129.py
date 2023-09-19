a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

if a>b:
    b, a = a, b
if a>c:
    c, a = a, c
if b>c:
    c, b = b, c

print(a, b ,c)