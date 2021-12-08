#Tính tổng các số chắn và lẻ
def tinh_tong_chan_le(n):
    tong_chan=0
    tong_le=0
    for i in range(1,n+1):
        if i%2==0:
            tong_chan+=i
        else:
            tong_le+=i
    return tong_chan,tong_le
#-----------------------------------------------    
n=int(input('Nhập n: '))
tong=tinh_tong_chan_le(n)
print('Tổng chẵn là:',tong[0])
print('Tổng lẽ là:',tong[1])