#https://onlinejudge.org/external/2/272.pdf

# UVA272 - TEX Quotes
import sys
now=True

for line in sys.stdin:
    ans=""
    
    for ch in line:
        if ch =='"':
            if now:
                ans+="``"
            else:
                ans+="''"
            now =not now
        else:
            ans+=ch
    
    print(ans,end="")