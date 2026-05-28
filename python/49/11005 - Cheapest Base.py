#11005 - Cheapest Base
#https://onlinejudge.org/external/110/11005.pdf

import sys

tokens = sys.stdin.read().split()
idx = 0

a = int(tokens[idx])  # 測資數量
idx += 1

for case in range(1, a + 1):
    b = []  # 36 個數字的成本

    for _ in range(36):
        b.append(int(tokens[idx]))
        idx += 1

    c = int(tokens[idx])  # 查詢數量
    idx += 1

    print(f"Case {case}:")

    for _ in range(c):
        d = int(tokens[idx])  # 要轉換的數字
        idx += 1

        ans = []
        best = 10**18

        # 試 base 2 到 base 36
        for e in range(2, 37):
            f = d
            cost = 0

            # 特別處理數字 0
            if f == 0:
                cost = b[0]
            else:
                while f > 0:
                    cost += b[f % e]
                    f //= e

            if cost < best:
                best = cost
                ans = [e]
            elif cost == best:
                ans.append(e)

        print(f"Cheapest base(s) for number {d}:", *ans)

    if case != a:
        print()