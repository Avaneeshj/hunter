a=int(input())
b=[]
c=0
while(a>0):
    c=a%10
    a=a//10
    b.append(c)
b=b[::-1]
for i in range(len(b)-1):
    c+=sum(b)
    b.pop(-1)
print(c)
