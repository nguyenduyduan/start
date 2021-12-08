s=str(input('Nhập số nhị phân: '))
n=0
for i in range(len(s)):
    n=int(s[i])*(2**(len(s)-1-i))+n
print(n)