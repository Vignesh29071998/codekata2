a=input()
dic={'V':5,'I':1,'X':10}
s=0
if len(a)==1:
    if a[0]=='I':print(dic['I'])
    elif a[0]=='V':print(dic['V'])
    else:print(dic['X'])
elif len(a)==2:
        if a[0]=='I':
            if a[1]=='V':
                s=4
            elif a[1]=='X':
                s=9
            elif a[1]=='I':
                s=2
        else:
            s=dic[a[1]]+dic[a[0]]
        print(s)
elif len(a)==3:
    if a[0]=='I':
        if a[1]=='I' and a[2]=='I':
            s=3
    elif a[0]=='V':
        if a[1]=='I' and a[2]=='I':
            s=7
    elif a[0]=='X':
        if a[1]=='I' and a[2]=='V':
            s=14
        elif a[1]=='I' and a[2]=='X':
            s=19
        else:
            s=dic['X']+dic[a[1]]+dic[a[2]]
    print(s)
elif len(a)==4:
    if a[0]=='V' and a[1]=='I' and a[2]=='I' and a[3]=='I':
        s=8
    else:
        s=17
    print(s)
else:
    print('18')
