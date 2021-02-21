# zip을 사용할 줄 아냐 모르냐 이므로 zip 사용법 꼭 알아두기

def solution(participant, completion):
    participant.sort()
    completion.sort()

    answer = ""
    for i, j in zip(participant,completion):
        if i != j:
            answer = i
            return answer
    answer = participant[-1]        
    return answer

 