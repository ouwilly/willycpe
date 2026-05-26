# 10050
T = int(input())

for _ in range(T):
    n = int(input())
    p = int(input())

    h = []
    for _ in range(p):
        h.append(int(input()))

    days = set()

    for x in h:
        for day in range(x, n + 1, x):
            if day % 7 != 6 and day % 7 != 0:
                days.add(day)

    print(len(days))