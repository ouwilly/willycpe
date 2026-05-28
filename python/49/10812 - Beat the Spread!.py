#10812 - Beat the Spread!
#https://onlinejudge.org/external/108/10812.pdf

import sys

tokens = sys.stdin.read().split()

a = int(tokens[0])  # 測資數量
idx = 1

for _ in range(a):
    b = int(tokens[idx])      # 兩隊分數總和
    c = int(tokens[idx + 1])  # 兩隊分數差
    idx += 2

    if b < c or (b + c) % 2 != 0:
        print("impossible")
    else:
        d = (b + c) // 2
        e = (b - c) // 2
        print(d, e)