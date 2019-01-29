d={}
l1,l2=input().split()
for i in range(0,len(l1)):
    if l1[i] not in d.keys():
        d[l1[i]]=l2[i]
    else:
        if d[l1[i]]!=l2[i]:
            print('no')
            break
else:
    print('yes')

