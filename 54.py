a=int(input())
b=list(map(int,input().split()))
c=[]
d=[]
for i in range(len(b)):
    c=b[:i+1]
    d.append(min(c))
print(*d,end="")
