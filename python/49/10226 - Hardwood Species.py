#10226 - Hardwood Species
#https://onlinejudge.org/external/102/10226.pdf

import sys

tokens = sys.stdin.read().splitlines()

a = int(tokens[0])  # 測資數量
idx = 2             # 第 1 行是測資數，第 2 行是空白行

for case in range(a):
    b = {}      # 統計樹名
    c = 0       # 總樹木數量

    # 讀到空白行，代表這組結束
    while idx < len(tokens) and tokens[idx] != "":
        d = tokens[idx]
        b[d] = b.get(d, 0) + 1
        c += 1
        idx += 1

    # 跳過空白行
    idx += 1

    if case > 0:
        print()

    # 樹名照字母順序輸出
    for d in sorted(b):
        e = b[d] * 100 / c
        print(f"{d} {e:.4f}")