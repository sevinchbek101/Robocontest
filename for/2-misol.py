a,b = map(int,input().split())
s = 0

for i in range(a,b + 1):
    s += 1
    print(i, end = " ")
print(f'\n{s}')