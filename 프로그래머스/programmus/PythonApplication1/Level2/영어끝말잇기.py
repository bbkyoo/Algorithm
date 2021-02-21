def solution(n, words):
    temp = 1
    num = 1
    answer = [0,0]

    if len(words[0]) == 1:
        answer = [1,1]
    else:
        for i in range(1, len(words)):
            temp += 1

            if len(words[i]) == 1:
                answer[0] = temp
                answer[1] = num
                break
            elif words[i-1][-1] != words[i][0]: 
                answer[0] = temp
                answer[1] = num
                break
            elif words[i] in words[:i]: 
                answer[0] = temp
                answer[1] = num
                break

            if temp == n:
                num += 1
                temp = 0

    return answer









