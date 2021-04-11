needs = [ [ 1, 0, 0 ], [1, 1, 0], [1, 1, 0], [1, 0, 1], [1, 1, 0], [0, 1, 1] ]
r = 2

cnt = [0] * len(needs)  

for i in range(len(needs)):
    if needs[i].count(1) <= r:
        idx = []
        for j in range(len(needs[i])):
            if needs[i][j] == 1:
                idx.append(j)
        
        idx_t = []
        for k in range(len(needs)):
            for j in range(len(needs[k])):
                if needs[k][j] == 1:
                    idx_t.append(j)

            isTrue = True
            for t in idx_t:
                if t not in idx:
                    isTrue = False
                    break

            if isTrue:
                cnt[i] += 1   
                
print(cnt)