print('Nhap so tram: ')
n = int (input())
listA=[]
listB=[]

for i in range (n):
    newlist=[]
    for j in range(i):
        newlist.append(' ')
    listA.append(newlist)

for i in range (1,n+1):
    print('Hang thu: ',i)
    newlist=[]
    for j in range (i,n+1):
        print('Nhap khoang cach cua tram', i ,'va tram', j , ': ')
        newlist.append(int(input()))
    listB.append(newlist)


for i in range (n):
    listA[i]+=listB[i]

for i in range (n):
    for j in range (n):
        listA[j][i]=listA[i][j]

for i in range (n):
    print(listA[i])


