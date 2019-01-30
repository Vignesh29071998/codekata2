n,k=map(int,input().split())
input()
n1=list(map(int,input().split()))
k1=list(map(int,input().split()))
k2=[]
for i in k1:
  n1.append(i)
  k2.append(max(n1))
for i in range(0,len(k2)):
  if i==len(k2)-1:
    print(k2[i])
  else:
    print(k2[i],end=' ')

