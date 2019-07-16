a,b=map(int,input().split())
c=list(map(int,input().split()))
d=0
for i in range(a):
    for j in range(a):
        if(j>i):
            if(abs(c[i]-c[j])==b):
                d+=1
print(d)
            
