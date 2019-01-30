a1,b1=map(int,input().split())
a2,b2=map(int,input().split())
a3,b3=map(int,input().split())
if a1==a2==a3:
  print('yes')
elif b1==b2==b3:
  print('yes')
elif a1==b1 and a2==b2 and a3==b3:
  print('yes')
else:
  print('no')
