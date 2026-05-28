#11063 - B2-Sequence
#https://onlinejudge.org/external/110/11063.pdf

import sys

tokens = sys.stdin.read().split()
idx = 0
case = 1

while idx < len(tokens):
    a = int(tokens[idx])  # 數列長度
    idx += 1

    b = []  # 存數列
    for _ in range(a):
        b.append(int(tokens[idx]))
        idx += 1

    ok = True

    # B2-Sequence 必須是正數且嚴格遞增
    for i in range(a):
        if b[i] <= 0:
            ok = False
        if i > 0 and b[i] <= b[i - 1]:
            ok = False

    c = set()  # 存所有兩兩相加的結果

    # 檢查 b[i] + b[j] 是否重複
    for i in range(a):
        for j in range(i, a):
            d = b[i] + b[j]

            if d in c:
                ok = False
            c.add(d)

    if ok:
        print(f"Case #{case}: It is a B2-Sequence.")
    else:
        print(f"Case #{case}: It is not a B2-Sequence.")

    print()
    case += 1