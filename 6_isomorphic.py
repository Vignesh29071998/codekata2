from collections import Counter
l1,l2=input().split()
a=Counter(l1)
b=Counter(l2)
a1,a2=[],[]
for i in a:
    a1.append(a[i])
for j in b:
    a2.append(b[j])
if a1==a2:
    print('yes')
else:
    print('no')

