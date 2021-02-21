from fractions import gcd

def solution(arr):
    answer = arr[0]
    for n in arr:
        answer = n * answer / gcd(n, answer)

    return answer

#def solution(arr):
#    arr.sort(reverse=True)

#    for i in range(len(arr)-1):
#        a = arr[i]
#        b = arr[i+1]
#        while a % b:
#            r = a % b
#            a = b
#            b = r
#        arr[i+1] = (arr[i]*arr[i+1])/b

#    return arr[-1]
