a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(a):
    if(a*(i+1)) in b:
        c+=1
print(c)
