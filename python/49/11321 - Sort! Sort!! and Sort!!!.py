#11321 - Sort! Sort!! and Sort!!!
#https://onlinejudge.org/external/113/11321.pdf

import sys

tokens = sys.stdin.read().split()
idx = 0

while True:
    a = int(tokens[idx])      # 數字個數
    b = int(tokens[idx + 1])  # mod 的數字
    idx += 2

    print(a, b)

    if a == 0 and b == 0:
        break

    c = []

    for _ in range(a):
        c.append(int(tokens[idx]))
        idx += 1

    def f(x):
        # Python 負數 % 會和 C 不一樣，所以這裡修正成 UVA 要的結果
        d = x % b
        if x < 0 and d != 0:
            d -= b

        # 奇數排前面
        if x % 2 != 0:
            e = 0
            g = -x   # 奇數大到小
        else:
            e = 1
            g = x    # 偶數小到大

        return (d, e, g)

    c.sort(key=f)

    for x in c:
        print(x)