import sys
from functools import reduce
print(len(list(filter(
    lambda x: int(x) % 2 == 0, reduce(
        lambda z, y: z + y, [open(z, "r").read().split() for z in sys.argv[1:]])
))))
