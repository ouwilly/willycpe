#12019 - Doom's Day Algorithm
#https://onlinejudge.org/external/120/12019.pdf

import sys

tokens = sys.stdin.read().split()

# 每個月的天數，2011 不是閏年
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 星期表，題目中 2011/1/1 是 Saturday
week = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]

a = int(tokens[0])
idx = 1

for _ in range(a):
    b = int(tokens[idx])      # 月
    c = int(tokens[idx + 1])  # 日
    idx += 2

    d = c

    # 把前面月份的天數加起來
    for e in range(1, b):
        d += month[e]

    # 用總天數 mod 7 找星期
    print(week[d % 7])