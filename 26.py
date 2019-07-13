a=int(input())
b=list(map(int,input().split()))
c=b[::-1]
print("->".join(map(str,c)))
