a=int(input())
b=list(map(int,input().split()))
for i in range(0,a):
    for j in range(i+1,a):
            for k in range(j+1,a):
                    if(b[i]+b[j]==b[k]):
                        print(b[i],b[j],b[k])
