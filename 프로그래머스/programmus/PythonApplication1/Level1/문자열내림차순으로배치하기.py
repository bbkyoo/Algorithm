def solution(s):    
    
    arr = []
    for i in range(len(s)):
        arr.append(s[i])

    arr.sort( reverse = True )

    answer = ''
    for i in range(len(arr)):
        answer += arr[i]
    
    return answer


