#11689：Soda Surpler
#https://onlinejudge.org/external/116/11689.pdf

import sys

tokens = sys.stdin.read().split()

a = int(tokens[0])
idx = 1

for _ in range(a):
    b = int(tokens[idx])
    c = int(tokens[idx + 1])
    d = int(tokens[idx + 2])
    idx += 3

    e = b + c
    ans = 0

    while e >= d:
        f = e // d
        ans += f
        e = f + e % d

    print(ans)