#948 - Fibonaccimal Base
#https://onlinejudge.org/external/9/948.pdf

import sys

tokens = sys.stdin.read().split()

# 先建立 Fibonacci 數列
fib = [1, 2]
while fib[-1] < 100000000:
    fib.append(fib[-1] + fib[-2])

a = int(tokens[0])

for i in range(1, a + 1):
    b = int(tokens[i])  # 原本的數字
    c = b               # 保留原數字用來輸出
    ans = ""

    # 從最大的 Fibonacci 數開始試
    for d in reversed(fib):
        if d <= b:
            ans += "1"
            b -= d
        elif ans != "":
            ans += "0"

    print(f"{c} = {ans} (fib)")