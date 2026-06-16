# https://onlinejudge.org/external/111/11150.pdf
import sys
tokens=sys.stdin.read().split()
it=iter(tokens)

for s in it:
    n=int(s)
    total=n
    empty=n
    
    while empty>=3:
        new=empty//3
        total+=new
        empty=new+(empty%3)
        
    if empty==2:
        total+=1
    
    print(total)