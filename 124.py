a=int(input())
b=[]
for i in range(a):
    b.append(1)
print(*b)
for i in range(a-1):
    b.pop(1)
    print(*b)
