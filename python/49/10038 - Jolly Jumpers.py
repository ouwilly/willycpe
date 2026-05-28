# 10038
import sys

tokens = sys.stdin.read().split()
it = iter(tokens)

while True:
    try:
        n = int(next(it))
        arr = [int(next(it)) for _ in range(n)]
    except StopIteration:
        break

    diff = {abs(arr[i] - arr[i + 1]) for i in range(n - 1)}

    print("Jolly" if diff == set(range(1, n)) else "Not jolly")