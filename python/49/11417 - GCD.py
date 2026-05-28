#11417 - GCD
#https://onlinejudge.org/external/114/11417.pdf

import sys
import math

tokens = sys.stdin.read().split()

for a in tokens:
    a = int(a)

    # 輸入 0 結束
    if a == 0:
        break

    b = 0

    # 枚舉所有 i < j 的組合
    for c in range(1, a):
        for d in range(c + 1, a + 1):
            b += math.gcd(c, d)

    print(b)