a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=0
if a>b:
    for i in range(b):
        if((d[i]) in c) and d.count(i)<=c.count(i):
            e+=1
        else:
            e=0
if(e==b):
    print("YES")
else:
    print("NO")
