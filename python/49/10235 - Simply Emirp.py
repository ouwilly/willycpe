#10235 - Simply Emirp
#https://onlinejudge.org/external/102/10235.pdf

import sys
import math

tokens = sys.stdin.read().split()

# 判斷質數
def is_prime(a):
    if a < 2:
        return False

    for b in range(2, int(math.sqrt(a)) + 1):
        if a % b == 0:
            return False

    return True


for a in tokens:
    b = int(a)              # 原本數字
    c = int(a[::-1])        # 反轉後的數字

    if not is_prime(b):
        print(f"{b} is not prime.")
    elif b != c and is_prime(c):
        print(f"{b} is emirp.")
    else:
        print(f"{b} is prime.")