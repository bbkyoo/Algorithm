def solution(s):
    s = s[2:-2]
    s = s.split("},{")

    s.sort(key = lambda x : len(x))
    answer = []

    for i in range(len(s)):
        temp = s[i].split(',')
        for j in range(len(temp)):
            if temp[j] not in answer:
                answer.append(temp[j])

    for i in range(len(answer)):
        answer[i] = int(answer[i])

    return answer
