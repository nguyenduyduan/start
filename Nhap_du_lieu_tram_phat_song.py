print('Nhap so tram: ')
n = int (input())
listA=[]
listB=[]
listC=[]
#Dòng tên trạm
for i in range (1,n+1):
    listC.append('tram'+str(i))
#Mục đích tạo các ô không cần nhập mà lấy từ các ô khác ví dụ có 1-2 thì 2-1 khỏi nhập
for i in range (n):
    newlist=[]
    for j in range(i):
        newlist.append(' ')
    listA.append(newlist)
#Khoảng cách của trạm i và trạm i
for i in range (n):
    listA[i].append('  0  ')
#Nhập vào các ô cần nhập vào
for i in range (1,n+1):
    print('Hang thu: ',i)
    newlist=[]
    for j in range (i+1,n+1):
        print('Nhap khoang cach cua tram', i ,'va tram', j , ': ')
        newlist.append('  '+str(int(input()))+'  ')
    listB.append(newlist)
#bảng sau nhập
for i in range (n):
    listA[i]+=listB[i]
#Bảng sau khi được lấp đầy
for i in range (n):
    for j in range (n):
        listA[j][i]=listA[i][j]
#In bảng ra
print('Bang khoang cach cac tram:')
print('     ',listC)
for i in range (n):
    print(listC[i],listA[i])
