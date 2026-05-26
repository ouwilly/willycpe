#10370
C=int(input())

for _ in range(C):
    data=list(map(int,input().split()))
    
    n=data[0]
    scorces=data[1:]
    
    avg=sum(scorces)/n
    count=0
    
    for scorce in scorces:
        if scorce> avg:
            count+=1
    
    percent=count/n*100
    
    print("{percent:.3f}%")