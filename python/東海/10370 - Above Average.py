#https://onlinejudge.org/external/103/10370.pdf
# UVA10370
# UVA10370 - Above Average
import sys

tokens = sys.stdin.read().split()
idx = 0

t = int(tokens[idx])
idx += 1

for _ in range(t):
    n = int(tokens[idx])
    idx += 1

    a = list(map(int, tokens[idx:idx+n]))
    idx += n

    avg = sum(a) / n
    cnt = sum(x > avg for x in a)

    print(f"{cnt / n * 100:.3f}%")