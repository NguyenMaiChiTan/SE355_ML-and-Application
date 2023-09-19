n = int(input("Nhap n: "))

flag = 1
t = n

while (t != 0):
    dv = t % 10
    if(dv % 2 == 1 ):
        flag = 0
    t = t / 10

if (flag):
    print("Toan chan")
else:
    print("Khong toan chan.")