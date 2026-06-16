# https://onlinejudge.org/external/101/10131.pdf
import sys

tokens = sys.stdin.read().split()
a = []

idx = 1
for i in range(0, len(tokens), 2):
    w = int(tokens[i])
    iq = int(tokens[i + 1])
    a.append((w, iq, idx))
    idx += 1

a.sort()

n = len(a)
dp = [1] * n
pre = [-1] * n

for i in range(n):
    for j in range(i):
        if a[j][0] < a[i][0] and a[j][1] > a[i][1]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                pre[i] = j

pos = 0
for i in range(n):
    if dp[i] > dp[pos]:
        pos = i

ans = []
while pos != -1:
    ans.append(a[pos][2])
    pos = pre[pos]

ans.reverse()

print(len(ans))
for x in ans:
    print(x)