n=int(input())
n1=list(input().split())
d={}
for i in n1:
  if i not in d:
    d[i]=1
  else:
    d[i]+=1
c=min(d,key=d.get)
print(d[c])
