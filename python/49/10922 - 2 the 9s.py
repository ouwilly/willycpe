#10922 - 2 the 9s
#https://onlinejudge.org/external/109/10922.pdf

import sys

tokens = sys.stdin.read().split()

for a in tokens:
    if a == "0":
        break

    b = a
    c = 0

    while len(b) > 1:
        d = 0
        for e in b:
            d += int(e)
        b = str(d)
        c += 1

    if b == "9":
        print(f"{a} is a multiple of 9 and has 9-degree {c}.")
    else:
        print(f"{a} is not a multiple of 9.")