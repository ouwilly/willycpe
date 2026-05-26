import sys

tokens = sys.stdin.read().split()

for x in tokens:
    n = int(x)

    if n == 0:
        break

    binary = bin(n)[2:]
    count = binary.count("1")

    print(f"The parity of {binary} is {count} (mod 2).")