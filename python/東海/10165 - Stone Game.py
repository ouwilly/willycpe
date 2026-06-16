#https://onlinejudge.org/external/101/10165.pdf
import sys

tokens=sys.stdin.read().split()
it=iter(tokens)

while True:
    n=int(next(it))
    if n==0:
        break
    x=0
    for  _ in range(n):
        x^=int(next(it))
    if x!=0:
        print("Yes")
    else:
        print("No")