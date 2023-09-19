x = abs(float(input("Nhap x: ")))
y = abs(float(input("Nhap y: ")))
z = abs(float(input("Nhap z: ")))

if x+y<z or x+z<y or y+z<x:
    print("Khong la tam giac!")
    exit()

if x==y and y==z:
    print("Tam giac deu!")
    exit()

def isHypo(a, b, h):
    if h*h == a*a + b*b:
        return True
    return False

if (isHypo(y, z, x) or isHypo(x, y, z) or isHypo(x, z, y)):
    if(x==y or y==z or z==x):
        print("Tam giac vuong can!")
    else:
        print("Tam giac vuong!")
else:
    if(x==y or y==z or z==x):
        print("Tam can!")
    else:
        print("Tam giac thuong!")

