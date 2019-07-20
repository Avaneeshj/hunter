a,b=list(map(list,input().split()))
c=len(a)
d=len(b)
f=[]
e=1
while(len(a)!=len(b)):
    if(c<d):
        a.append(e)
        e+=1
    elif(d<c):
        b.append(e)
        e+=1
for i in range(len(a)):
    for j in range(len(b)):
        if(i==j):
            g=str(a[i])+str(b[j])
            f.append(g)
print("".join(map(str,f)))
