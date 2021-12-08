print('Phương trình bậc nhất ax+b=0')
a=int(input('Nhập hệ số a: '))
b=int(input('Nhập hệ số b: '))
if a==0:
    if b==0:
        print('Phương trình vô số nghiệm')
    else:
        print('Phương trình vô số nghiệm')
else:
    x=-(b/a)
    print('Nghiệm của phương trình là: ',x)