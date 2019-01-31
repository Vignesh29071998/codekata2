l,r=map(int,input().split())
c=0
for i in range(l,r+1):
  k=i**(1/2)
  if int(k)==k:
    c+=1
print(c)
