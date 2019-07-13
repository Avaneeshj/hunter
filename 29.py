a=int(input())
b=list(map(int,input().split()))
b.sort()
c=b[::-1]
d=0
e=0
f=[]
for i in range(0,a):
    e+=c[d]
    f.append(e)
    d+=1
print(max(f))
