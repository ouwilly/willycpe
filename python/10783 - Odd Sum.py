T = int(input())

for case in range(1, T + 1):
    a = int(input())
    b = int(input())

    total = 0

    for i in range(a, b + 1):
        if i % 2 == 1:
            total += i

    print(f"Case {case}: {total}")