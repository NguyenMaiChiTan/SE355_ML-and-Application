num = abs(int(input("Nhap n: ")))

temp = num

while temp!=0:
    digit = temp % 10
    if digit%2 == 0:
        print(False)
        exit()
    temp= int(temp/10)

print(True)