#299 - Train Swapping
#https://onlinejudge.org/external/2/299.pdf

import sys

tokens = sys.stdin.read().split()

a = int(tokens[0])  # 測資數量
idx = 1

for _ in range(a):
    b = int(tokens[idx])  # 火車長度
    idx += 1

    c = []  # 火車排列
    for _ in range(b):
        c.append(int(tokens[idx]))
        idx += 1

    ans = 0

    # 算有幾組前面比後面大
    for d in range(b):
        for e in range(d + 1, b):
            if c[d] > c[e]:
                ans += 1

    print(f"Optimal train swapping takes {ans} swaps.")