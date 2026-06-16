import sys
tokens=sys.stdin.read().split()
it=iter(tokens)

for s in it:
    if s=="0:00":
        break
    h,m=s.split(":")
    h=int(h)
    m=int(m)
    minute=m*6
    hour=h*30+m*0.5
    
    diff=abs(hour-minute)
    ans=min(diff,360-diff)
    
    print(f"{ans:.3f}")