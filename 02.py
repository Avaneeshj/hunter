n=int(input())
a=input()
l=[]
for i in a:
    l.append(i)
b=set(l)
c=list(b)
c.sort()
d=[]
d=c[::-1]
print(''.join(map(str,d)))

