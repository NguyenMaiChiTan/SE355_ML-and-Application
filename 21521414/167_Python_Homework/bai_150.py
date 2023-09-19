a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
m = abs(a)
n = abs(b)

while (m*n != 0):
    if (n > m):
        n = n - m
    else:
        m = m -n 
bcnn = abs(a * b)/(m + n)
print("Kết quả: ", bcnn)

