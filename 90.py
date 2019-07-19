a=input()
b=c=0
for i in range(len(a)):
    b=1
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            b+=1
        else:
            break
    if b>c:
        c=b
        d=a[i]
print(d,c)
