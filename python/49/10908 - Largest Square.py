#10908 - Largest Square
#https://onlinejudge.org/external/109/10908.pdf

import sys

tokens = sys.stdin.read().split()
idx = 0

a = int(tokens[idx])  # 測資數量
idx += 1

for _ in range(a):
    b = int(tokens[idx])      # 列數
    c = int(tokens[idx + 1])  # 欄數
    d = int(tokens[idx + 2])  # 查詢數
    idx += 3

    e = []  # 存地圖

    for _ in range(b):
        e.append(tokens[idx])
        idx += 1

    print(b, c, d)

    for _ in range(d):
        f = int(tokens[idx])      # 中心列
        g = int(tokens[idx + 1])  # 中心欄
        idx += 2

        h = e[f][g]  # 中心字元
        ans = 1
        k = 1

        while True:
            top = f - k
            bottom = f + k
            left = g - k
            right = g + k

            # 超出邊界就停止
            if top < 0 or bottom >= b or left < 0 or right >= c:
                break

            ok = True

            # 檢查這個正方形範圍內是不是都等於中心字元
            for i in range(top, bottom + 1):
                for j in range(left, right + 1):
                    if e[i][j] != h:
                        ok = False

            if ok:
                ans += 2
                k += 1
            else:
                break

        print(ans)