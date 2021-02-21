# 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.
# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때
# 전체 학생의 수는 2명 이상 30명 이하입니다.
# 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

def solution(n, lost, reserve):
    student = [i for i in range(1, n+1)]

    lost.sort()
    reserve.sort()
    temp = []

    for i in range(len(reserve)):
        if reserve[i] in lost:
            temp.append(i)
            lost.pop(lost.index(reserve[i]))
    
    while temp:
        reserve.pop(temp[-1])
        temp.pop(-1)

    for i in range(len(lost)):
        if lost[i] in student:
            student.pop(student.index(lost[i]))

    for i in range(len(reserve)):
        for j in range(len(lost)):
            if (reserve[i]-1 == lost[j] or reserve[i]+1 == lost[j]) and (lost[j] not in student):
                student.append(lost[j])
                break
    
    answer = len(student)
    return answer

n = 5
lost = [2, 4]
reserve = [3]
print(solution(n, lost, reserve))

                
            

