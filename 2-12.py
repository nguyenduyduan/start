def nhap_du_lieu_hoc(m):
    ten_mon=[]
    so_tin_chi=[]
    diem_tb_mon=[]
    for i in range(m):
        ten_mon.append(str(input('Nhập tên môn học: ')))
        so_tin_chi.append(int(input('Nhập số tín chỉ của môn học: ')))
        diem_tb_mon.append(float(input('Nhập điểm trung bình của môn học: ')))
    return so_tin_chi,diem_tb_mon

def diem_tb_hoc(m,so_tin_chi,diem_tb_mon):
    tongdiem=0
    tinchi=0
    for i in range(m):
        tongdiem+=diem_tb_mon[i]*so_tin_chi[i]
        tinchi+=so_tin_chi[i]
    tb=tongdiem/tinchi
    return tb

def nhap_du_lieu_hs(n):
    ten_hs=[]
    drl=[]
    diem_hoc=[]
    for i in range(n):
        ten_hs.append(str(input('Nhập tên học sinh: ')))
        drl.append(int(input('Nhập điểm rèn luyện của học sinh: ')))
        m=int(input('Nhập số môn học: '))
        so_tin_chi,diem_tb_mon=nhap_du_lieu_hoc(m)
        tb=diem_tb_hoc(m,so_tin_chi,diem_tb_mon)
        diem_hoc.append(tb)
    return ten_hs,drl,diem_hoc

def tinh_diem_xet_hb(diem_hoc,drl):
    diem_xet_hb=[]
    for i in range(n):
        diem_xet_hb.append(round(diem_hoc[i]+0.2*drl[i],2))
    return diem_xet_hb

def tim_5_so_max(a,diem):
    max_5 = []
    added = []                             
    for i in range(len(diem)):
        added.append(0)                     
    for i in range(a):
        max = 0                            
        while (added[max] == 1):            
            max = max + 1
        for j in range(1,len(diem)):
            if added[j] == 0:               
                if diem[j]> diem[max]:      
                    max = j                
        max_5.append(diem[max])            
        added[max] = 1                      
    return max_5
#-------------------------------------------------------------------
n=int(input('Nhập số sinh viên: '))
if n<5:
    a=n
else:
    a=5
ten_sv,drl,diem_hoc=nhap_du_lieu_hs(n)
diem_xet_hb=tinh_diem_xet_hb(diem_hoc,drl)
max_5=tim_5_so_max(a,diem_xet_hb)
print(max_5)
for i in range(a):
    j=diem_xet_hb.index(max_5[i])
    print(i+1,'. Sinh viên',ten_sv[j],'nhận được học bổng với số điểm',diem_xet_hb[j])