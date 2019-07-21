a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(a):
    if(sum(b[0:i])==sum(b[i+1:])):
        c+=1
if(c>0):
    print("yes")
else:
    print("no")
