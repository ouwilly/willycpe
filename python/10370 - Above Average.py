C = int(input())

for _ in range(C):
    data = list(map(int, input().split()))

    n = data[0]
    scores = data[1:]

    avg = sum(scores) / n

    count = 0
    for score in scores:
        if score > avg:
            count += 1

    percent = count / n * 100

    print(f"{percent:.3f}%")