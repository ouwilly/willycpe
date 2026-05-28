#10929 You can say 11

import sys

tokens = sys.stdin.read().split()

for n in tokens:
    if n == "0":
        break

    total = 0

    for i in range(len(n)):
        if i % 2 == 0:
            total += int(n[i])
        else:
            total -= int(n[i])

    if total % 11 == 0:
        print(n, "is a multiple of 11.")
    else:
        print(n, "is not a multiple of 11.")