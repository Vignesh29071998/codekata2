n=int(input())
s=list(input())
for i in s:
  if i in ['a','e','i','o','u','A','E','I','O','U']:
    s.remove(i)
a=s[::-1]
for i in range(0,len(a)):
  if i==len(a)-1:
    print(a[i])
  else:
    print(a[i],end='')
