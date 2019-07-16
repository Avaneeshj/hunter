a=int(input())
b=list(map(int,input().split()))
for i in range(a):
    if(b.count(b[i])==1):
        print(b[i])
