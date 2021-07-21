#def solution(progresses, speeds):
#    arr = []

#    for i in range(len(progresses)):
#        result = progresses[i]
#        count = 0
#        while result < 100:
#            result += speeds[i]
#            count += 1
#        arr.append(count)

#    cnt = 0
#    temp = arr[0]
#    answer = []
#    for i in range(1,len(arr)):
#        if temp < arr[i]:
#            cnt += 1
#            answer.append(cnt)
#            if i == len(arr)-1: 
#                answer.append(1)
#            else:
#                cnt = 0
#                temp = arr[i]
#        else:
#            cnt += 1
#            if i == len(arr)-1:
#                cnt += 1
#                answer.append(cnt)
#    return answer

def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer















