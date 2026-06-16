# https://onlinejudge.org/external/103/10300.pdf
import sys

tokens = sys.stdin.read().split()
it = iter(tokens)

t = int(next(it))

for _ in range(t):
    n = int(next(it))
    total = 0

    for _ in range(n):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))

        total += a * c

    print(total)