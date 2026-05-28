#10189 - Minesweeper
#https://onlinejudge.org/external/101/10189.pdf

import sys

tokens = sys.stdin.read().split()
idx = 0
case = 1

while True:
    a = int(tokens[idx])      # 高度
    b = int(tokens[idx + 1])  # 寬度
    idx += 2

    if a == 0 and b == 0:
        break

    c = []  # 地圖
    for _ in range(a):
        c.append(tokens[idx])
        idx += 1

    if case > 1:
        print()

    print(f"Field #{case}:")

    # 八個方向
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(a):
        ans = ""

        for j in range(b):
            if c[i][j] == "*":
                ans += "*"
            else:
                cnt = 0

                # 檢查周圍 8 格
                for k in range(8):
                    x = i + dx[k]
                    y = j + dy[k]

                    if 0 <= x < a and 0 <= y < b and c[x][y] == "*":
                        cnt += 1

                ans += str(cnt)

        print(ans)

    case += 1