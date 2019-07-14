a=list(input())
c=len(a)-1
b=0
for i in range(c):
    if(a[:i]==a[i+1:]):
        b+=1
if(b>0):
    print("YES")
else:
    print("NO")
        
