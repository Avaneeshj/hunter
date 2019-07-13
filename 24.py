a,b=map(int,input().split())
c=list(map(int,input().split()))
d=0
for i in range(a):
    for j in range(a):
        if(i<j):
            if(c[i]+c[j]==b):
                d+=1
if(d>0):
    print("YES")
else:
    print("NO")
