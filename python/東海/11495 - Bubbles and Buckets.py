# https://onlinejudge.org/external/114/11495.pdf
import sys

tokens = sys.stdin.read().split()
idx = 0

while True:
    n = int(tokens[idx])
    idx += 1

    if n == 0:
        break

    a = [0] + list(map(int, tokens[idx:idx+n]))
    idx += n

    cnt = 0
    for i in range(1, n + 1):
        while a[i] != i:
            j = a[i]
            a[i], a[j] = a[j], a[i]
            cnt += 1

    if cnt % 2:
        print("Marcelo")
    else:
        print("Carlos")