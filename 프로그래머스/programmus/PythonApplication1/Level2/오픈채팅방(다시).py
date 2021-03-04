def solution(record):
    answer = []
    userdict = {}

    for i in record:
        if (i.split(' ')[0] == "Enter") | (i.split(' ')[0] == "Change"):
            userdict[i.split(' ')[1]] = i.split(' ')[2]

    for i in record:
        if i.split(' ')[0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(userdict[i.split(' ')[1]]))

        elif i.split(' ')[0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(userdict[i.split(' ')[1]]))
    
        else:
            pass
    
    return answer




























