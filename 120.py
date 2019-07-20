a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(a):
    for j in range(a):
        if(i<j):
            d=b[i]+b[j]
            if d in b:
                e=b.index(d)
                if(j<e):
                    c+=1
print(c)
