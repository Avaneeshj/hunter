a=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(a):
    for j in range(a):
        if(j>i):
            c.append(b[j]-b[i])
print(max(c))
