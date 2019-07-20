c=int(input())
a=[]
a.append(1)
b=1
for i in range(100000//2):
    b+=b
    a.append(b)
if c in a:
    print("YES")
else:
    print("NO")
