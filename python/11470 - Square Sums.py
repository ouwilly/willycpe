#11470 - Square Sums
#https://onlinejudge.org/external/114/11470.pdf

import sys

tokens = sys.stdin.read().split()
idx = 0
case = 1

while True:
    n = int(tokens[idx])
    idx += 1

    if n == 0:
        break

    a = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(tokens[idx]))
            idx += 1
        a.append(row)

    ans = []

    # 總共有 (n + 1) // 2 圈
    for layer in range((n + 1) // 2):
        top = layer
        bottom = n - 1 - layer
        left = layer
        right = n - 1 - layer

        s = 0

        # 如果只剩中間一格
        if top == bottom and left == right:
            s += a[top][left]
        else:
            # 上排
            for j in range(left, right + 1):
                s += a[top][j]

            # 下排
            for j in range(left, right + 1):
                s += a[bottom][j]

            # 左邊，不含上下角落
            for i in range(top + 1, bottom):
                s += a[i][left]

            # 右邊，不含上下角落
            for i in range(top + 1, bottom):
                s += a[i][right]

        ans.append(str(s))

    print(f"Case {case}: {' '.join(ans)}")
    case += 1