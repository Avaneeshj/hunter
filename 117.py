a=list(input())
b=0
for i in range(len(a)):
    z=a[i]
    c=int(z)**i
    b+=c
print(b)
