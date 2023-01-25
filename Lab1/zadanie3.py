import sys

n = len(sys.argv)

for j in range(1, n):
    i = sys.argv[j]
    f = 0
    for c in i:
        if c > '9' or c < '0':
            f = 1
    if f == 1:
        continue

    i = int(i)

    if i < 2:
        continue
    if i == 2:
        print(i)
    else:
        if i % 2 == 0:
            continue
        q = pow(i, 0.5)
        j = 3
        while j <= q:
            if i % j == 0:
                break
            j += 2
        else:
            print(i)
