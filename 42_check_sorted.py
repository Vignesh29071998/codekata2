a=int(input())
b=list(map(int,input().split()))
if b==sorted(b):
  print('yes')
else:
  print('no')
