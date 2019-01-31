n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
  if i==k:
    c=1
    break
  else:
    c=0
if c==1:
  print('Yes')
else:print('No')
