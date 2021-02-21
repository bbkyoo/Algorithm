import sys

input = sys.stdin.readline

#n = int(input())
#s_n = int(input())
#student = list(map(int, input().split()))
#q = []

#if n > s_n:
#    for i in range(s_n):
#        q.append([student[i], 1])
#else:
#    for i in range(n):
#        q.append([student[i], 1])

#    for i in range(n, len(student)):
#        isTrue = False
#        for j in range(n):
#            if student[i] == q[j][0]:
#                isTrue = True
#                q[j][1] += 1
#                break

#        if isTrue:
#            continue
#        else:
#            idx = 0
#            for j in range(n):
#                if q[idx][1] > q[j][1]:
#                    idx = j
#            q.pop(idx)
#            q.append([student[i], 1])

#q.sort()
#result = str(q[0][0])

#for i in range(1,len(q)):
#    result += " " + str(q[i][0])

#print(result)

n = int(input())
w = int(input())

num = list(map(int, input().split()))

photo = dict()
for i in range(w):
    if num[i] in photo:
        photo[num[i]][0] += 1
    else:
        if len(photo) < n:
            photo[num[i]] = [1, i]
        else:
            del_list = sorted(photo.items(), key = lambda x : (x[1][0], x[1][1]))
            del_key = del_list[0][0]
            del(photo[del_key])
            photo[num[i]] = [1, i]

ans_list = list(sorted(photo.keys()))
answer = str(ans_list[0])
for i in ans_list[1: ]:
    answer += " " + str(i)
print(answer)


















