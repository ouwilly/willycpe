T = int(input())
for t in range(T):
    n = list(map(int, input().split()))
    v = n[1:]
    v.sort()
    mid = v[n[0] // 2]
    res = 0
    for i in v:
        res += abs(i - mid)
    print(res)