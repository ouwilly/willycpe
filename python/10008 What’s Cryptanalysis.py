import sys

n = int(input())

count = {}

for _ in range(n):
    line = input()

    for ch in line:
        if ch.isalpha():
            ch = ch.upper()

            if ch not in count:
                count[ch] = 0

            count[ch] += 1

items = list(count.items())

items.sort(key=lambda x: (-x[1], x[0]))

for ch, num in items:
    print(ch, num)