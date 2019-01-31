s1,s2,k=input().split()
c=0
for i in range(0,len(s1)):
  if s1[i]!=s2[i]:
    c+=1
if c==int(k):
  print('yes')
else:
  print('no')
