a=list(input())
b=[]
for i in range(len(a)):
    if(a.count(a[i])==1):
        b.append(a[i])
print("".join(map(str,b)))
