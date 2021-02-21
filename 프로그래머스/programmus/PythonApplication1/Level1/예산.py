def solution(d, budget):    
    
    d.sort()
    
    k = 0
    while len(d) > k:
        if budget < 0 or budget < d[k]:
            break

        budget = budget - d[k]
        k += 1

    return k

