#10415 - Eb Alto Saxophone Player
#https://onlinejudge.org/external/104/10415.pdf

import sys

tokens = sys.stdin.read().splitlines()

a = int(tokens[0])

# 每個音對應要按的手指
mp = {
    "c":  "0111001111",
    "d":  "0111001110",
    "e":  "0111001100",
    "f":  "0111001000",
    "g":  "0111000000",
    "a":  "0110000000",
    "b":  "0100000000",
    "C":  "0010000000",
    "D":  "1111001110",
    "E":  "1111001100",
    "F":  "1111001000",
    "G":  "1111000000",
    "A":  "1110000000",
    "B":  "1100000000",
}

for i in range(1, a + 1):
    b = tokens[i]

    c = [0] * 10      # 目前手指是否按著
    ans = [0] * 10    # 每根手指按下次數

    for d in b:
        e = mp[d]

        for f in range(10):
            # 原本沒按，現在要按，才算一次
            if c[f] == 0 and e[f] == "1":
                ans[f] += 1

            c[f] = int(e[f])

    print(*ans)