#https://onlinejudge.org/external/100/10019.pdf

import sys
tokens=sys.stdin.read().split()
it=iter(tokens)

t=int(next(it))

for _ in range(t):
    n=int(next(it))
    
    b1=bin(n).count("1")
    b2=bin(int(str(n),16)).count("1")
    
    print(b1,b2)