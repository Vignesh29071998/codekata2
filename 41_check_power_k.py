n,k=map(int,input().split())
i=k
while i<10000:
  i=i*k
  if i==n:
    print('yes')
    break
  else:
    if i>n:
      print('no')
      break
    
  
