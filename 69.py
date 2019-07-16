a=list(input())
b=0
i=[".","c","o","m"]
if "@" and "." in a:
    c=a.count("@")
    d=a.index("@")
    e=a.count(".")
    f=a.index(".")
if(c==1 and e==1):
    g=f-d
    if(g>3 and d>2):
        h=a[-4:]
        if(i==h):
            b+=1
if(b>0):
    print("YES")
else:
    print("NO")
