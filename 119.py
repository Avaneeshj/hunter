a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(a):
    for j in range(a):
        if(i<j):
            if(b[i]<b[j]):
                c+=1
print(c)
