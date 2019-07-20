a=list(input())
b=list(input())
c=[]
y=len(a)
z=len(b)
x=y-z
w=z-y
if(x>w):
    for n in range(x):
        b.append(" ")
elif(w>x):
    for n in range(w):
        a.append(" ")
for i in range(len(a)):
    for j in range(len(b)):
        if(i==j):
            d=str(b[j])+str(a[i])
            c.append(d)
for i in range(len(c)):
    print(c[i])
            
