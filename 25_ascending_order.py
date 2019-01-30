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
li1=sorted(d,key=d.get)
for i in range(0,len(li1)):
  if i==len(li1)-1:
    print(li1[i])
  else:
    print(li1[i],end=' ')

  

  
  

  

  
  
