print('Nhap so tram: ')
n=int(input())
lst=[]

for i in range (n):
    print('Hang thu: ',i+1)
    newlst=[]
    for j in range (n):
        print('Nhap khoang cach: ')
        newlst.append(int(input()))
    lst.append(newlst)

for i in range (len(lst)):
    print(lst[i])