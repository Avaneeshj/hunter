a=list(input())
b=[]
c=0
for i in range(len(a)):
    b=a[:i]+a[i+1:]
    if(b[:]==b[::-1]):
        c+=1
if(c>0):
    print("YES")
else:
    print("NO")
