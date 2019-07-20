a = int(input())
for i in range(a):
    t = pow(2, i)
    if t == a:
        print('YES')
        exit(0)
    elif t > a:
        break
print('NO')
