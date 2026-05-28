#10056 - What is the Probability?
#https://onlinejudge.org/external/100/10056.pdf

import sys

tokens = sys.stdin.read().split()

a = int(tokens[0])  # 測資數量
idx = 1

for _ in range(a):
    b = int(tokens[idx])        # 玩家數量
    c = float(tokens[idx + 1])  # 每次成功機率
    d = int(tokens[idx + 2])    # 目標玩家編號
    idx += 3

    # 如果成功機率是 0，永遠不會有人贏
    if c == 0:
        print("0.0000")
    else:
        e = 1 - c

        # 第 d 個玩家贏的機率
        ans = (e ** (d - 1) * c) / (1 - e ** b)

        print(f"{ans:.4f}")