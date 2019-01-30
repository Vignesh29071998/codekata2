n,k=map(int,input().split())
a=[]
for i in range(1,100000):
  if n%i==0 and k%i==0:
    a.append(i)
print(max(a))
