#tính tổng
def tinh_tong(n):
    tong=0
    for i in range (1,n+1):
        tong += i
    return tong
#tính giai thừa
def tinh_giai_thua(n):
    giai_thua=1
    for i in range (1,n+1):
        giai_thua *= i
    return giai_thua
#----------------------------------------------------
n=int(input('Nhập n: '))
tong=tinh_tong(n)
giai_thua=tinh_giai_thua(n)
print('Giai thừa của',n,'là:',giai_thua)
print('Tổng của',n,'số đầu tiên là:',tong)