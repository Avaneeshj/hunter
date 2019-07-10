a=int(input())
a=list(map(int,input().split()))
a.sort()
a.reverse()
if a[0]==0:
    print("0")
else:
    for l in a:
        print(l,end='')
