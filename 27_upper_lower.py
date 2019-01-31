s=input()
k=''
for i in s:
  if i.islower():
    k+=i.upper()
  else:
    k+=i.lower()
print(k)
