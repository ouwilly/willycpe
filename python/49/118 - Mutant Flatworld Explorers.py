#118 - Mutant Flatworld Explorers
#https://onlinejudge.org/external/1/118.pdf

import sys

tokens = sys.stdin.read().split()
idx = 0

a = int(tokens[idx])
b = int(tokens[idx + 1])
idx += 2

dirs = "NESW"
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

scent = set()

while idx < len(tokens):
    c = int(tokens[idx])
    d = int(tokens[idx + 1])
    e = dirs.index(tokens[idx + 2])
    f = tokens[idx + 3]
    idx += 4

    lost = False

    for g in f:
        if g == "L":
            e = (e - 1) % 4
        elif g == "R":
            e = (e + 1) % 4
        else:
            x = c + dx[e]
            y = d + dy[e]

            if x < 0 or x > a or y < 0 or y > b:
                if (c, d) in scent:
                    continue
                scent.add((c, d))
                lost = True
                break

            c = x
            d = y

    if lost:
        print(c, d, dirs[e], "LOST")
    else:
        print(c, d, dirs[e])