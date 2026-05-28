#10170 - The Hotel with Infinite Rooms
#https://onlinejudge.org/external/101/10170.pdf
import sys

tokens = sys.stdin.read().split()
idx = 0

while idx < len(tokens):
    a = int(tokens[idx])      # 起始天數 / 起始人數
    b = int(tokens[idx + 1])  # 目標總人數
    idx += 2

    c = a
    d = 2000000000

    # 二分搜尋答案
    while c < d:
        e = (c + d) // 2

        # 從 a 加到 e 的總和
        f = (a + e) * (e - a + 1) // 2

        if f >= b:
            d = e
        else:
            c = e + 1

    print(c)