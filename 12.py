n,k=map(int,input().split())
a=list(map(int,input().split()))
b=[]
c=[]
for i in range(n):
    b.append(a[i])
b.sort()
c=b[::-1]
print(c[k-1])
