import sys

tokens = sys.stdin.read().split()

for x in tokens:
    n = int(x)

    ans = n

    while n >= 3:
        new_cola = n // 3
        ans += new_cola
        n = new_cola + n % 3

    if n == 2:
        ans += 1

    print(ans)