a,b=map(int,input().split())
c=list(map(int,input().split()))[:a]
d=0
for i in range(len(c)):
    if c[i]<=b:
       d+=1
print(d)
