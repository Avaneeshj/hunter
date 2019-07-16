a=int(input())
b=list(map(int,input().split()))
b.append(100001)
c=[]
for i in range(a):
    if b[i]>b[i+1]:
        b[i]=b[i+1]
        c.append(b[i])
    else:
        c.append(-1)
print(*c,end="")
