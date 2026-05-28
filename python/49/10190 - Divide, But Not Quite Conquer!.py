#10190 - Divide, But Not Quite Conquer!
#https://onlinejudge.org/external/101/10190.pdf

import sys

tokens = sys.stdin.read().split()
idx = 0

while idx < len(tokens):
    a = int(tokens[idx])      # n
    b = int(tokens[idx + 1])  # m
    idx += 2

    c = []        # 存過程
    d = a         # 目前的數字
    ok = True

    # m 必須大於 1，n 也要大於 1
    if b <= 1 or a <= 1:
        ok = False
    else:
        while d > 1:
            c.append(d)

            # 如果不能整除，就失敗
            if d % b != 0:
                ok = False
                break

            d //= b

        c.append(1)

    if ok:
        print(*c)
    else:
        print("Boring!")