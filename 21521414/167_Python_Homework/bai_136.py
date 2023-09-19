x = int(input("Nhap nam bat dau: "))
y = int(input("Nhap nam ket thuc: "))

year = x
for year in range(x, y+1):
    if (year%4==0 and year%100!=0) or year%400==0:
        print(year)
    

