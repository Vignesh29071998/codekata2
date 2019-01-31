#hello
s=input()
d={}
for i in s:
  if i not in d:
    d[i]=1
  else:
    d[i]+=1
try:
  if d['(']==d[')']:
    print('yes')
  else:
    print('no')
except KeyError:
  print('no')
    
