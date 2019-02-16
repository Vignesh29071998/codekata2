s1,s2=input().split()
for i in range(0,(len(s1)-len(s2))+1):
  if s1[i:i+len(s2)]==s2:
    print('yes')
    break
else:
  print('no')
