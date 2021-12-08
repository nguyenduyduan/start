n = int(input('Nhap so nguyen duong n: '))
bin=''
if n==0:
    print('số nhị phân tương ứng là:','0')
elif n>0:
    while n:
        bin=bin+str(n%2)
        n=int((n-n%2)/2)
    print('số nhị phân tương ứng là:',bin)
else :
    print('Không phải số nguyên dương')