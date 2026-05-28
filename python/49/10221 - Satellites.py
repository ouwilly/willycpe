#10221 - Satellites
#https://onlinejudge.org/external/102/10221.pdf

import sys
import math

tokens = sys.stdin.read().split()
idx = 0

while idx < len(tokens):
    a = float(tokens[idx])       # 衛星離地表高度
    b = float(tokens[idx + 1])   # 角度
    c = tokens[idx + 2]          # deg 或 min
    idx += 3

    # 地球半徑 6440，加上衛星高度
    d = a + 6440

    # 如果單位是 min，要除以 60 變成度
    if c == "min":
        b = b / 60

    # 角度超過 180，要用較小的那邊
    if b > 180:
        b = 360 - b

    # 角度轉弧度
    e = math.radians(b)

    # 弧長 = 半徑 * 弧度
    f = d * e

    # 弦長 = 2 * 半徑 * sin(角度 / 2)
    g = 2 * d * math.sin(e / 2)

    print(f"{f:.6f} {g:.6f}")