num = abs(int(input("Nhap n: ")))

if num==1:
    print(f"{num} khong phai la so nguyen to!")
    exit()
    
for i in range(2, num):
    if num%i==0:
        print(f"{num} khong phai la so nguyen to!")
        exit()

print(f"{num} la so nguyen to!")