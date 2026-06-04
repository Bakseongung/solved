def solution(signals):
    cycles=[]
    t=1
    for G,Y,R in signals:
        cycles.append(G+Y+R)
    
    while t<3200000:
        flag=True
        
        for i,(G,Y,R) in enumerate(signals):
            cycle=cycles[i]
            cnt=t%cycle
            
            
            #노란불 X
            if not (G <= cnt < G+Y):
                flag=False
                break
                
        t+=1
        if flag:
            return t 
    
    #노란불 X
    return -1
