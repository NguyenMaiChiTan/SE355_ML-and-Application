num = abs(int(input("Nhap n: ")))

sum = 0

for i in range(1, num):
    if num%i==0:
        sum+=i

if sum==num:
    print(f"{num} la so hoan thien!")
else:
    print(f"{num} khong phai la so hoan thien!")
    