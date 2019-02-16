a=input()
b=''
if len(a)<3:
  b+=a[0]
else:
  for i in range(0,len(a),3):
    if i==0:
      b+=a[0]
    else:
      b+=a[i]
print(b)
    
  
