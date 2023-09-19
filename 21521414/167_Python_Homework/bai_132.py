As = list(map(float, input("Nhap Xa, Ya: ").split()))
Bs = list(map(float, input("Nhap Xb, Yb: ").split()))
Cs = list(map(float, input("Nhap Xc, Yc: ").split()))
Ms = list(map(float, input("Nhap Xm, Ym: ").split()))

def calArea(As, Bs, Cs):
    return abs(As[0]*Bs[1] + Bs[0]*Cs[1] + Cs[0]*As[1] -
           As[1]*Bs[0] + Bs[1]*Cs[0] + Cs[1]*As[0]) / 2

Sabc = calArea(As, Bs, Cs)
Smab = calArea(As, Bs, Ms)
Smbc = calArea(Ms, Bs, Cs)
Smac = calArea(As, Ms, Cs)

S = Smab + Smac + Smbc
if(S == Sabc):
    print("M trong tam giac!")
else:
    print("M ngoai tam giac!")
    