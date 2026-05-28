
#https://onlinejudge.org/external/1/100.pdf
import sys

tokens = sys.stdin.read().split()
it = iter(tokens)

memo = {1: 1}

def cycle(n):
    if n in memo:
        return memo[n]

    if n % 2 == 1:
        memo[n] = 1 + cycle(3 * n + 1)
    else:
        memo[n] = 1 + cycle(n // 2)

    return memo[n]

for a, b in zip(it, it):
    i = int(a)
    j = int(b)

    start = min(i, j)
    end = max(i, j)

    ans = 0
    for n in range(start, end + 1):
        length = cycle(n)
        if length > ans:
            ans = length

    print(i, j, ans)