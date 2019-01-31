a=input()
flag=0
for i in range(0,len(a)-1):
    if a[i]==' ' and a[i+1]==' ':
        flag=0
        break
    else:
        flag=1
if flag==1:
    print(a)
else:
    b=a.split()
    print(''.join(b))
