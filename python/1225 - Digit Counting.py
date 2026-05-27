#https://onlinejudge.org/external/12/1225.pdf?utm_source=chatgpt.com
import sys

tokens = sys.stdin.read().split()
t = int(tokens[0])

for k in range(1, t + 1):
    n = int(tokens[k])
    cnt = [0] * 10

    for i in range(1, n + 1):
        for ch in str(i):
            cnt[int(ch)] += 1

    print(*cnt)