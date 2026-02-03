a = float(input())
s = 1

for i in range(5):
    s += 0.2
    print(f"{a * s:.2f}",end = " ")