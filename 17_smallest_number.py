l,r=map(int,input().split())
for i in range(2,100001):
  if i%l==0 and i%r==0:
    print(i)
    break
    
