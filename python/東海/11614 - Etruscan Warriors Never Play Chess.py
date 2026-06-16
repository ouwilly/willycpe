# https://onlinejudge.org/external/116/11614.pdf
import sys
import math

tokens = sys.stdin.read().split()
it = iter(tokens)

t = int(next(it))

for _ in range(t):
    n = int(next(it))
    ans = (math.isqrt(1 + 8*n) - 1) // 2
    print(ans)