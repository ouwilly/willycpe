#10000 - Longest Paths
#https://onlinejudge.org/external/100/10000.pdf

import sys
sys.setrecursionlimit(999999)

t = sys.stdin.read().split()
i = 0
c = 1

while True:
    n = int(t[i]); i += 1
    if n == 0:
        break

    s = int(t[i]); i += 1
    g = [[] for _ in range(n + 1)]

    while True:
        a = int(t[i]); b = int(t[i+1]); i += 2
        if a == b == 0:
            break
        g[a].append(b)

    d = {}

    def f(x):
        if x in d:
            return d[x]
        ans = (0, x)
        for y in g[x]:
            l, e = f(y)
            if l + 1 > ans[0] or l + 1 == ans[0] and e < ans[1]:
                ans = (l + 1, e)
        d[x] = ans
        return ans

    l, e = f(s)
    print(f"Case {c}: The longest path from {s} has length {l}, finishing at {e}.")
    print()
    c += 1