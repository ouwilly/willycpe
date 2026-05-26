import sys

tokens = sys.stdin.read().split()
it = iter(tokens)

for x in it:
    if x == "0":
        break

    while len(x) > 1:
        total = 0

        for ch in x:
            total += int(ch)

        x = str(total)

    print(x)