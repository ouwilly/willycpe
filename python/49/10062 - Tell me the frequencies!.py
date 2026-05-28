#10062 - Tell me the frequencies!
#https://onlinejudge.org/external/100/10062.pdf
import sys

tokens = sys.stdin.read().splitlines()

first = True

for a in tokens:
    if not first:
        print()
    first = False

    b = {}

    # 統計每個字元出現次數
    for c in a:
        d = ord(c)
        b[d] = b.get(d, 0) + 1

    # 先依照次數小到大，再依照 ASCII 大到小
    e = sorted(b.items(), key=lambda x: (x[1], -x[0]))

    for f, g in e:
        print(f, g)