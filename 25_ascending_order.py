n=int(input())
li=list(input().split())
a=[]
i=0
for i in range(len(li)):
    for j in range(0,len(li)-i-1):
        if len(li[j])>len(li[j+1]):
            li[j],li[j+1]=li[j+1],li[j]
for i in range(len(li)-1):
    if len(li[i])==len(li[i+1]) and li[i]>li[i+1]:
        li[i],li[i+1]=li[i+1],li[i]
print(*li)


  

  
  

  

  
  
