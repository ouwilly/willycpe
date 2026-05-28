#10242 - Fourth Point!!
#https://onlinejudge.org/external/102/10242.pdf

import sys

tokens = sys.stdin.read().split()
idx = 0

while idx < len(tokens):
    a = float(tokens[idx])
    b = float(tokens[idx + 1])
    c = float(tokens[idx + 2])
    d = float(tokens[idx + 3])
    e = float(tokens[idx + 4])
    f = float(tokens[idx + 5])
    g = float(tokens[idx + 6])
    h = float(tokens[idx + 7])
    idx += 8

    p1 = (a, b)
    p2 = (c, d)
    p3 = (e, f)
    p4 = (g, h)

    # 找出重複的點
    if p1 == p3:
        x = p2[0] + p4[0] - p1[0]
        y = p2[1] + p4[1] - p1[1]
    elif p1 == p4:
        x = p2[0] + p3[0] - p1[0]
        y = p2[1] + p3[1] - p1[1]
    elif p2 == p3:
        x = p1[0] + p4[0] - p2[0]
        y = p1[1] + p4[1] - p2[1]
    else:
        x = p1[0] + p3[0] - p2[0]
        y = p1[1] + p3[1] - p2[1]

    print(f"{x:.3f} {y:.3f}")