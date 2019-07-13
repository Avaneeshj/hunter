a,b=map(int,input().split())
e=[]
for i in range(a):
    c=set(map(int,input().split()))
    e.append(c)
print(*c.intersection(*e))

