a=int(input())
b=list(map(int,input().split()))
c,d=map(int,input().split())
e=[]
f=[]
g=[]
j=b
for i in range(len(b)):
    if(b[i]==c):
        e.append(i)
for i in range(len(j)):
    if(b[i]==d):
        g.append(i)
for i in range(len(e)):
    for j in range(len(g)):
        f.append(abs(e[i]-g[j]))
print(min(f))

