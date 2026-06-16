#https://onlinejudge.org/external/103/10340.pdf

# UVA10340 - All in All
import sys

tokens = sys.stdin.read().split()
it = iter(tokens)

for a, b in zip(it, it):
    idx = 0

    for ch in b:
        if idx < len(a) and ch == a[idx]:
            idx += 1

    if idx == len(a):
        print("Yes")
    else:
        print("No")