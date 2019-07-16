a=int(input())
b=[1000,500,100,50,10,1]
c=0
while(a>0):
    for i in range(len(b)):
        if a>=b[i]:
            a=a-b[i]
            c+=1
print(c)
