import sys
tokens=sys.stdin.read().split()
it=iter(tokens)

for s in it:
    n=int(s)
    half=n//2
    base=10**half
    limit=10**n
    
    for x in range(limit):
        left=x//base
        right=x%base
        
        if(left+right)**2==x:
            print(f"{x:0{n}d}")