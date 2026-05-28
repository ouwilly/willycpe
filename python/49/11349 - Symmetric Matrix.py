#11349 - Symmetric Matrix
#https://onlinejudge.org/external/113/11349.pdf

import sys

tokens = sys.stdin.read().split()

a = int(tokens[0])  # 測資數量
idx = 1

for case in range(1, a + 1):
    b = tokens[idx]      # 讀掉 N
    c = tokens[idx + 2]  # 矩陣大小
    idx += 3

    c = int(c)
    d = []

    # 讀入 c*c 個數字
    for _ in range(c * c):
        d.append(int(tokens[idx]))
        idx += 1

    ok = True

    # 檢查有沒有負數
    for e in d:
        if e < 0:
            ok = False

    # 檢查前後是否對稱
    for e in range(len(d)):
        if d[e] != d[len(d) - 1 - e]:
            ok = False

    if ok:
        print(f"Test #{case}: Symmetric.")
    else:
        print(f"Test #{case}: Non-symmetric.")