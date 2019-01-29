n=input()
s=''
for i in range(0,len(n)):
  if i%2==0:
    s+=n[i+1]
  else:
    s+=n[i-1]
print(s)
