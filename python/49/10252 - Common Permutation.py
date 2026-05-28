#10252 - Common Permutation
#https://onlinejudge.org/external/102/10252.pdf
import sys

tokens = sys.stdin.read().splitlines()
idx = 0

while idx < len(tokens):
    a = tokens[idx]       # 第一個字串
    b = tokens[idx + 1]   # 第二個字串
    idx += 2

    ans = ""

    # 從 a 到 z 檢查共同出現幾次
    for c in range(26):
        d = chr(ord("a") + c)

        # 取兩個字串中 d 出現次數較少的
        e = min(a.count(d), b.count(d))

        ans += d * e

    print(ans)