#10101 - Bangla Numbers
#https://onlinejudge.org/external/101/10101.pdf
import sys

tokens = sys.stdin.read().split()

# 把數字 a 轉成 Bangla 表示法
def bangla(a):
    b = []

    # kuti = 10000000
    if a >= 10000000:
        b += bangla(a // 10000000)
        b.append("kuti")
        a %= 10000000

    # lakh = 100000
    if a >= 100000:
        b.append(str(a // 100000))
        b.append("lakh")
        a %= 100000

    # hajar = 1000
    if a >= 1000:
        b.append(str(a // 1000))
        b.append("hajar")
        a %= 1000

    # shata = 100
    if a >= 100:
        b.append(str(a // 100))
        b.append("shata")
        a %= 100

    # 剩下的數字
    if a > 0:
        b.append(str(a))

    return b


case = 1

for a in tokens:
    a = int(a)

    b = bangla(a)

    # 題目要求 Case 編號寬度 4
    print(f"{case:4d}.", end="")

    if len(b) == 0:
        print(" 0")
    else:
        print(" " + " ".join(b))

    case += 1