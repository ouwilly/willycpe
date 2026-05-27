import sys
tokens=sys.stdin.read().split()
a=int(tokens[0])

for i in range(1,a+1):
    b=int(tokens[i])
    c=bin(b).count("1")
    d=bin(int(str(b),16)).count("1")
    
    print(c,d)    