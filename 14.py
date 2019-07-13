from itertools import permutations
a=input()
b=permutations(a)
for i in list(b):
    print("".join(i))
