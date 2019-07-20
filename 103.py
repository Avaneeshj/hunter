a=int(input())
b=[1]
print(*b)
for i in range(a-1):
    b.append(1)
    b.append(1)
    print(*b)
