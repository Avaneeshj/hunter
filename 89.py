a=input()
b=[]
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
c=b[::-1]
print("".join(map(str,c)))
