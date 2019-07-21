a=input()
b=''
for i in range(0,len(a)-1,2):
    if(int(a[i+1])%2==0):
        b+=a[i]*int(a[i+1])
    else:
        b+=a[i]+a[i+1]
print(b)
