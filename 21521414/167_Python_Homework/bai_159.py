n = int(input("Nhap n: "))
lc = int(n % 10)
dem = 0
t = n
while(t != 0):
    dv = t % 10
    if (lc >= dv):
        lc = dv
    t = t // 10

t = n

while(t != 0):
    dv = int(t % 10)
    if (dv == lc):
        dem = dem + 1
    t = t // 10

print("Đếm = ", dem)