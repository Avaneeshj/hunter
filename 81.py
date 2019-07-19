a=int(input())
d=0
e=[]
for i in range(a):
    if(len(str(i))==1):
        d+=1
    else:
        e=list(str(i))
        z=0
        for j in range(0,len(e)-1):
            if(abs(int(e[j])-int(e[j+1]))==1):
                z+=1
            else:
                break
            if z==len(e)-1:
                d+=1
print(d)
