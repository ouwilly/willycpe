import sys

tokens = sys.stdin.read().split()
it = iter(tokens)

while True:
    try:
        a = int(next(it))
        b = int(next(it))
    except StopIteration:
        break

    print(abs(a - b))