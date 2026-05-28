#490 - Rotating Sentences
#https://onlinejudge.org/external/4/490.pdf

import sys

tokens = sys.stdin.read().splitlines()

# 找出最長的一行有多長
a = 0
for b in tokens:
    a = max(a, len(b))

# 從第 0 欄開始，一欄一欄輸出
for c in range(a):
    ans = ""

    # 從最後一行往第一行看
    for d in range(len(tokens) - 1, -1, -1):
        if c < len(tokens[d]):
            ans += tokens[d][c]
        else:
            ans += " "

    print(ans)