# https://onlinejudge.org/external/1/151.pdf
import sys

tokens = sys.stdin.read().split()

for s in tokens:
    n = int(s)
    if n == 0:
        break

    m = 1
    while True:
        a = list(range(1, n + 1))
        idx = 0

        while len(a) > 1:
            a.pop(idx)
            idx = (idx + m - 1) % len(a)

        if a[0] == 13:
            print(m)
            break

        m += 1