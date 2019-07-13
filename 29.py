a=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(a):
         d=b[i:]
         c.append(sum(d))
print(max(c))
