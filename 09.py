a=int(input())
b=list(map(int,input().split()))
for i in range(a):
    for j in range(i+1,a):
        if(b[i]+b[j]==0):
            print(b[i],b[j])
