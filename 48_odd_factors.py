n = int(input())
a = []
if n%2 == 0:
  for i in range(1,n):
    if n%i == 0 and (i==1 or i==2):
      a.append(i)
    elif n%i == 0 and i%2!=0:
      a.append(i)
else:
  for i in range(1,n+1):
    if n%i == 0 and (i==1 or i==2):
      a.append(i)
    elif n%i == 0 and i%2!=0:
      a.append(i)

print(*a)
