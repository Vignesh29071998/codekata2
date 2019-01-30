n,k=map(int,input().split())
n1=list(map(int,input().split()))
a=len(n1)-k
l=n1[a:]+n1[:a]
for i in range(0,len(l)):
  if i==len(l)-1:
    print(l[i])
  else:
    print(l[i],end=' ')
