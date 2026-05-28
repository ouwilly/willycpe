#10642
#https://onlinejudge.org/external/106/10642.pdf

import sys

tokens = sys.stdin.read().split()

a = int(tokens[0])  # 測資數量
idx = 1

# 把座標轉成它在路徑中的第幾格
def f(b, c):
    d = b + c
    return d * (d + 1) // 2 + b

for case in range(1, a + 1):
    b = int(tokens[idx])
    c = int(tokens[idx + 1])
    d = int(tokens[idx + 2])
    e = int(tokens[idx + 3])
    idx += 4

    # 起點位置
    x = f(b, c)

    # 終點位置
    y = f(d, e)

    print(f"Case {case}: {y - x}")