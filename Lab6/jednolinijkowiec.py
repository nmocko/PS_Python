import sys
from collections import Counter

print(dict(Counter([len(word) for word in sys.stdin.read().split()])))

# d = {}
# for x in [len(word) for word in sys.stdin.read().split()]: d[x] = d.get(x, 0) + 1
# print(d)
