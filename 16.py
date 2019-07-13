a,b=map(int,input().split())
c=list(map(int,input().split()))
d=[[abs(i-b),i] for i in c]
d.sort()
d=d[1:]
e=[i[1] for i in d[:3]]
print(*e)
