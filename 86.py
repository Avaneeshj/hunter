a=int(input())
b=[]
for i in range(a+1):
    c=i
    if(len(str(c))==1):
        b.append(i)
    else:
        while(c>0):
            d=c%10
            c=c//10
            b.append(d)
print(b.count(2))
