from itertools import combinations

def bitwiseEquations(a, b):
    
    result = []
    
    for i in range(len(a)):
        isTrue = True
        mx = max(a[i], b[i])
        arr = []
        for k in range(mx+1):
            arr.append(k)

        temp = sorted(list(set(combinations(arr, 2))))
        
        for j in range(len(temp)):        
            if temp[j][0] + temp[j][1] == a[i] and temp[j][0] ^ temp[j][1] == b[i]: 
                result.append((2*temp[j][0])+(3*temp[j][1]))
                isTrue = False
                break

        if isTrue:
            result.append(0)

    return result

a = [15, 139]
b = [15, 75]
print(bitwiseEquations(a, b))
   








