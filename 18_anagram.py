n=int(input())
a=[]
b='kabali'
c=0
b=sorted(b)
for i in range(0,n):
  a.append(input())
for i in a:
  if b==sorted(i):
    c+=1
print(c)
  
