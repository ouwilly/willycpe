#10093 - An Easy Problem!
#https://onlinejudge.org/external/100/10093.pdf
import sys

tokens = sys.stdin.read().splitlines()

for a in tokens:
    a = a.strip()

    if a == "":
        continue

    b = []  # 存每個字元轉成的數字

    for c in a:
        if c.isdigit():          # 0~9
            b.append(int(c))
        elif c.isupper():        # A~Z -> 10~35
            b.append(ord(c) - ord("A") + 10)
        elif c.islower():        # a~z -> 36~61
            b.append(ord(c) - ord("a") + 36)

    d = max(b) + 1  # 最小 base 至少要比最大數字大
    e = sum(b)      # 各位數總和
    ans = -1

    # base 最小是 2，最大是 62
    for f in range(max(2, d), 63):
        if e % (f - 1) == 0:
            ans = f
            break

    if ans == -1:
        print("such number is impossible!")
    else:
        print(ans)