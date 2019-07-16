a,b=map(int,input().split())
c=list(map(int,input().split()))
for i in range(a):
    if b in c:
        c.remove(b)
if(len(c)>0):
    print(*c,end="")
else:
    print("empty")
