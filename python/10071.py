import sys

tokens=sys.stdin.read().split()
it=iter(tokens)

while True:
    try:
        v=int(next(it))
        t=int(next(it))
    except StopIteration:
        break
    
    print(2*v*t)