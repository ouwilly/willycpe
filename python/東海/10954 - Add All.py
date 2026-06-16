# https://onlinejudge.org/external/109/10954.pdf
import sys
import heapq

tokens = sys.stdin.read().split()
idx = 0

while True:
    n = int(tokens[idx])
    idx += 1

    if n == 0:
        break

    a = list(map(int, tokens[idx:idx+n]))
    idx += n

    heapq.heapify(a)
    ans = 0

    while len(a) > 1:
        x = heapq.heappop(a)
        y = heapq.heappop(a)
        ans += x + y
        heapq.heappush(a, x + y)

    print(ans)