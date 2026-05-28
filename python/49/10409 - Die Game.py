#10409 - Die Game
#https://onlinejudge.org/external/104/10409.pdf

import sys

tokens = sys.stdin.read().split()
i = 0

while True:
    a = int(tokens[i])
    i += 1

    if a == 0:
        break

    top = 1
    north = 2
    west = 3
    east = 4
    south = 5
    bottom = 6

    for _ in range(a):
        b = tokens[i]
        i += 1

        if b == "north":
            top, north, bottom, south = south, top, north, bottom
        elif b == "south":
            top, south, bottom, north = north, top, south, bottom
        elif b == "east":
            top, east, bottom, west = west, top, east, bottom
        elif b == "west":
            top, west, bottom, east = east, top, west, bottom

    print(top)