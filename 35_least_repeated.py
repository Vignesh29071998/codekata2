a=input().split()
s=''
d={}
b=[]
for i in a:
  s+=i.lower()
for i in s:
  if i not in d:
    d[i]=1
  else:
    d[i]+=1
p=d[min(d,key=d.get)]
for i in d:
  if d[i]==p:
    b.append(i)
print(*b)
