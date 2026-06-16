import sys

lines = sys.stdin.read().splitlines()

for i in range(0, len(lines), 2):
    x = int(lines[i])
    a = list(map(int, lines[i + 1].split()))

    ans = 0
    n = len(a) - 1

    for j in range(n):
        ans = ans * x + a[j] * (n - j)

    print(ans)