n=int(input())
flag,c=0,0
a,b=[],[]
for i in range(2,n):
  if n%i==0:
    flag=1
    break
  else:
    flag=0
if flag==0:
  print(n)
else:
  for i in range(2,n+1):
    if n%i==0:
      a.append(i)
  for i in a:
    if i==2:
      b.append(i)
    else:
      for k in range(2,i):
        if i%k==0:
          c=1
          break
        else:
          c=0
      if c==0:
        b.append(i)
  for i in range(0,len(b)):
    if i==len(b)-1:
      print(b[i])
    else:
      print(b[i],end=' ')
      
