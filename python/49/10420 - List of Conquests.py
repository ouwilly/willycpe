#10420 - List of Conquests
#https://onlinejudge.org/external/104/10420.pdf

import sys

tokens = sys.stdin.read().splitlines()

a = int(tokens[0])  # 人數 / 資料筆數
b = {}              # 統計國家出現次數

for i in range(1, a + 1):
    c = tokens[i].split()[0]  # 每行第一個字是國家
    b[c] = b.get(c, 0) + 1

# 國家名稱照字母順序輸出
for c in sorted(b):
    print(c, b[c])