#10268 - 498'
#https://onlinejudge.org/external/102/10268.pdf

import sys

tokens = sys.stdin.read().splitlines()
idx = 0

while idx < len(tokens):
    # 第一行是 x
    a = int(tokens[idx])
    idx += 1

    # 第二行是多項式係數
    b = list(map(int, tokens[idx].split()))
    idx += 1

    c = len(b) - 1  # 最高次方
    ans = 0

    # 導函數係數：
    # b[0] * c, b[1] * (c-1), ...
    for d in range(c):
        ans = ans * a + b[d] * (c - d)

    print(ans)