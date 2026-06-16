#https://onlinejudge.org/external/101/10127.pdf

# UVA10127 - Ones
import sys

tokens = sys.stdin.read().split()

for s in tokens:
    n = int(s)
    x = 1
    cnt = 1

    while x % n != 0:
        x = (x * 10 + 1) % n
        cnt += 1

    print(cnt)