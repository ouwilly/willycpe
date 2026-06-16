#https://onlinejudge.org/external/2/299.pdf

import sys

tokens = sys.stdin.read().split()
it = iter(tokens)

t = int(next(it))

for _ in range(t):
    n=int(next(it))
    a=[]
    
    for _ in range(n):
        a.append(int(next(it)))
    cnt=0
        
    for i in range(n):
        for j in range(n-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                cnt+=1
    print(f"Optimal train swapping takes {cnt} swaps.")