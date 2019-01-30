n=int(input())
d={}
li=input().split()
a=[]
m=0
for i in li:
  s=0
  for j in range(0,len(i)):
     s+=ord(li[m][j])
  m+=1
  d[i]=s
print(sorted(d,key=d.get))

  

  
  
