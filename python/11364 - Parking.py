#11364 - Parking
#https://onlinejudge.org/external/113/11364.pdf

import sys

tokens = sys.stdin.read().split()

a = int(tokens[0])  # 測資數量
idx = 1

for _ in range(a):
    b = int(tokens[idx])  # 商店數量
    idx += 1

    c = []  # 存商店位置

    for _ in range(b):
        c.append(int(tokens[idx]))
        idx += 1

    # 從最左走到最右，再走回來
    print((max(c) - min(c)) * 2)