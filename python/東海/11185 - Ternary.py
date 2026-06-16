# https://onlinejudge.org/external/111/11185.pdf
import sys

tokens = sys.stdin.read().split()

for s in tokens:
    n = int(s)

    if n < 0:
        break

    if n == 0:
        print(0)
        continue

    ans = ""

    while n > 0:
        ans = str(n % 3) + ans
        n //= 3

    print(ans)