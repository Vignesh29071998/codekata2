n1,n2=input().split()
c=0
for i in range(0,len(n1)):
  if n1[i]!=n2[i]:
    c+=1
if c==1:
  print('yes')
else:
  print('no')
