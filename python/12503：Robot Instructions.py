#12503
#https://onlinejudge.org/external/125/12503.pdf

import sys

data = sys.stdin.read().splitlines()
t = int(data[0])
idx = 1

for _ in range(t):
    n = int(data[idx])
    idx += 1

    moves = []
    pos = 0

    for _ in range(n):
        s = data[idx]
        idx += 1

        if s == "LEFT":
            moves.append(-1)
        elif s == "RIGHT":
            moves.append(1)
        else:
            moves.append(moves[int(s.split()[-1]) - 1])

        pos += moves[-1]

    print(pos)