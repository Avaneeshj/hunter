a=int(input())
b=list(map(int,input().split()))
c=b
d=[]
while(len(c)!=1):
    for i in range(len(c)):
        if i%2!=0:
            d.append(c[i])
    c=d
    d=[]
print(b.index(c[0]))
