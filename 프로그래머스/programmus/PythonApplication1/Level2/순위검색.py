# 시간초과

# https://dev-note-97.tistory.com/131

#def solution(info, query):
#    answer = [0]*len(query)

#    info_temp = []
#    query_temp = []
#    for i in range(len(info)):
#        info_temp.append(info[i].split(" "))

#    for i in range(len(query)):
#        query_temp.append(query[i].split("and"))

#    q_temp = []
#    for i in range(len(query_temp)):
#        temp = []
#        for j in range(len(query_temp[i])):
#            if query_temp[i][j] != query_temp[i][-1]:
#                temp.append(query_temp[i][j].strip())
#            else:
#                w = query_temp[i][-1].split()
#                temp.append(w[0].strip())
#                temp.append(w[1].strip())
#        q_temp.append(temp)            

#    for i in range(len(q_temp)):
#        for j in range(len(info_temp)):
#            isTrue = True
#            for k in range(4):
#                if q_temp[i][k] == info_temp[j][k] or q_temp[i][k] == '-':
#                    pass
#                else:
#                    isTrue = False
#                    break

#            if isTrue and int(info_temp[j][-1]) >= int(q_temp[i][-1]):
#                answer[i] += 1

#    return answer





















