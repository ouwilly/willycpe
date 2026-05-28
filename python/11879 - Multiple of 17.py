#11879 - Multiple of 17
#https://onlinejudge.org/external/118/11879.pdf

import sys

tokens = sys.stdin.read().split()

for a in tokens:
    # 輸入 0 結束
    if a == "0":
        break

    b = 0  # 目前餘數

    # 一位一位算餘數，避免大數字爆掉
    for c in a:
        b = (b * 10 + int(c)) % 17

    if b == 0:
        print(1)
    else:
        print(0)