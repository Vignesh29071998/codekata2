n=input()
n=n.lower()
s=''
for i in n:
  if ord(i)+3>122:
    k=(ord(i)+3)-122
    s+=chr(96+k)
  else:
    s+=chr(ord(i)+3)
print(s.upper())
