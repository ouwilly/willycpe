#10127 - Ones
#https://onlinejudge.org/external/101/10127.pdf
import sys

tokens = sys.stdin.read().split()

for a in tokens:
    a = int(a)

    b = 1      # 目前的餘數
    c = 1      # 目前用了幾個 1

    # 如果還不能整除，就繼續在右邊補一個 1
    while b % a != 0:
        b = (b * 10 + 1) % a
        c += 1

    print(c)