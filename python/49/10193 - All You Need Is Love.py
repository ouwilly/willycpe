#10193 - All You Need Is Love
#https://onlinejudge.org/external/101/10193.pdf

import sys
import math

tokens = sys.stdin.read().split()

a = int(tokens[0])  # 測資數量
idx = 1

for case in range(1, a + 1):
    b = tokens[idx]      # 第一個二進位字串
    c = tokens[idx + 1]  # 第二個二進位字串
    idx += 2

    # 把二進位字串轉成十進位整數
    d = int(b, 2)
    e = int(c, 2)

    # 如果 gcd 大於 1，代表有共同因數
    if math.gcd(d, e) > 1:
        print(f"Pair #{case}: All you need is love!")
    else:
        print(f"Pair #{case}: Love is not all you need!")