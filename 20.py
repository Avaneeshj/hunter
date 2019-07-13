def ip(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a,b=map(int,input().split())
c=0
for i in range(a,b+1):
    d=bin(i).count('1')
    if ip(d):
        c+=1
print(c)
