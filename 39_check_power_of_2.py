a=int(input())
if a==1 or a==2:
  print('yes')
else:
  i=2
  while i<10000:
    i=i*2
    if i==a:
      print('yes')
      break
    else:
      if i>a:
        print('no')
        break
