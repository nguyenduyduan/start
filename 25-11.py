def diem_khoi(a,b,c):
    return a*2+b+c
def nhap_diem(mon):
    diem=[]
    for i in range(len(mon)):
        x=float(input('Nhập điểm môn '+mon[i]+': '))
        diem.append(x)
    return diem
def tong_diem_max(lst):
    tong_max=lst[0]
    d=0
    for i in range(1,len(lst)):
        if tong_max <= lst[i]:
            tong_max=lst[i]
            d=i
    vt=[]
    for i in range(len(lst)):
        if tong_max==lst[i]:
            vt.append(i)
    return vt
#------------------------------------------
mon=['Toán', 'Lý', 'Hóa', 'Sinh', 'Văn', 'Sử', 'Địa', 'Anh']
diem=nhap_diem(mon) 
# Khối a : toán, lý, hóa (toán x 2)
khoi_a=diem_khoi(diem[0],diem[1],diem[2])
# khối b : toán, hóa, sinh (sinh x 2)
khoi_b=diem_khoi(diem[3],diem[0],diem[2])
# Khối c : văn, sử, địa (văn x 2)
khoi_c=diem_khoi(diem[4],diem[5],diem[6])
# khối d : toán, văn, anh (anh x 2)
khoi_d=diem_khoi(diem[7],diem[4],diem[0])
lst=[khoi_a,khoi_b,khoi_c,khoi_d]
print(lst)
lst_khoi=['khối a','khối b','khối c','khối d']
vt=tong_diem_max(lst)
for i in vt:
    print('Bạn nên thi',lst_khoi[i])