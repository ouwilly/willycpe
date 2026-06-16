# https://onlinejudge.org/external/104/10407.pdf
import sys
import math

for line in sys.stdin.read().splitlines():
    a = list(map(int, line.split()))

    if a == [0]:
        break

    a.pop()   # 拿掉每行最後的 0

    ans = 0
    for x in a[1:]:
        ans = math.gcd(ans, abs(x - a[0]))

    print(ans)