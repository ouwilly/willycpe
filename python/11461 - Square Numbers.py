# 11461
import math

while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    ans = math.isqrt(b) - math.isqrt(a - 1)

    print(ans)