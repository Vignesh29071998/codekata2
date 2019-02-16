a,b=input().split()
a=list(a)
i=0
while i<int(b):
  c=a.pop(0)
  a.append(c)
  i+=1
print(''.join(a))
