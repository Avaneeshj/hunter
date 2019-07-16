a,b=map(int,input().split())
c=list(map(int,input().split()))
for i in range(b):
    c=c[1:]+c[:1]
print(*c,end="")
