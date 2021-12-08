a=int(input('Nhap canh cua tam giac: '))
b=int(input('Nhap canh cua tam giac: '))
c=int(input('Nhap canh cua tam giac: '))
if (a+b>c) and (a+c>b) and (b+c>a):
    print('Ba canh cua tam giac')
    cv=a+b+c
    p=cv/2
    s=(p*(p-a)*(p-b)*(p-c))**(1/2)
    print('Chu vi: ',cv)
    print('Dien tich: ',s)
else:
    print('Canh khong hop li')