a=int(input())
g=len(str(a))
c=0
while(a>0):
    b=a%10
    c+=b
    a=int(a/10)
h=len(str(c))
d=[]
f=0
for i in range(h):
    e=c%10
    d.append(e)
    c=int(c/10)
if(d[:]==d[::-1]):
    print("YES")
else:
    print("NO")
