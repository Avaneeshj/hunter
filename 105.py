a=int(input())
b=0
d=len(str(a))
for i in range(a):
    c=a%10
    a=a//10
    b+=c**d
print(b)
