s=str(input('Nhập ngày tháng năm: '))

kt=False
while kt==False:
    kt=True
    dem=0
    for i in range(len(s)):
        if s[i]=='/':
            dem+=1
        if s[0]=='/'or s[len(s)-1]=='/':
            kt=False
            s=str(input('Ngày tháng năm không hợp lệ hãy nhập lại: '))
    if dem!=2:
        kt=False
        s=str(input('Ngày tháng năm không hợp lệ hãy nhập lại: '))
    d,m,y=s.split('/')
    
d31=[1,3,5,7,8,10,12]
d30=[4,6,9,11]
if int(m) in d31:
    print('Tháng có 31 ngày')
elif int(m) in d30:
    print('Tháng có 30 ngày')
elif int(m)==2:
    if int(y)%100==0:
        if int(y)%400==0:
            print('Tháng có 29 ngày')
        else:
            print('Tháng có 28 ngày')
    elif int(y)%4==0:
        print('Tháng có 29 ngày')
    else:
        print('Tháng có 28 ngày')