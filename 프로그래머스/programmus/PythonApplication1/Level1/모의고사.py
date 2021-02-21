# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5,           1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5,            2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5,          3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

def solution(answers):
    no_math1 = []
    no_math2 = []
    no_math3 = []
    
    for i in range(len(answers)):
        if i % 5 == 0 :
            no_math1.append(1)
        elif i % 5 == 1:
            no_math1.append(2)
        elif i % 5 == 2:
            no_math1.append(3)
        elif i % 5 == 3:
            no_math1.append(4)
        elif i % 5 == 4:
            no_math1.append(5)

        if i % 8 == 1 :
            no_math2.append(1)
        elif i % 8 == 3:
            no_math2.append(3)
        elif i % 8 == 5:
            no_math2.append(4)
        elif i % 8 == 7:
            no_math2.append(5)
        elif i % 2 == 0:
            no_math2.append(2)
        
        if i % 10 == 0 or i % 10 == 1:
            no_math3.append(3)
        elif i % 10 == 2 or i % 10 == 3:
            no_math3.append(1)
        elif i % 10 == 4 or i % 10 == 5:
            no_math3.append(2)
        elif i % 10 == 6 or i % 10 == 7:
            no_math3.append(4)
        elif i % 10 == 8 or i % 10 == 9:
            no_math3.append(5)    
                

    count1 = 0
    count2 = 0
    count3 = 0

    for i in range(len(answers)):
        if answers[i] == no_math1[i]:
            count1 += 1
        if answers[i] == no_math2[i]:
            count2 += 1
        if answers[i] == no_math3[i]:
            count3 += 1

    answer = []
    if count1 > count2 and count1 > count3:
        answer.append(1)
    elif count2 > count1 and count2 > count3:
        answer.append(2)
    elif count3 > count1 and count3 > count2:
        answer.append(3)
    elif count2 == count1 and count2 > count3:
        answer.append(1)
        answer.append(2)
    elif count3 == count1 and count1 > count2:
        answer.append(1)
        answer.append(3)
    elif count2 == count3 and count2 > count1:
        answer.append(2)
        answer.append(3)
    elif count2 == count3 and count2 == count1:
        answer.append(1)
        answer.append(2)
        answer.append(3)

    return answer

# [1,3,2,4,2]
answers = [1,3,2,4,2]
print(solution(answers))