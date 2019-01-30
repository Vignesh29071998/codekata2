n,k=map(int,input().split())
n1=list(map(int,input().split()))
a=len(n1)-k
print(n1[a:]+n1[:a])
