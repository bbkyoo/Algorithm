def rotate(matrix):
    copy_matrix = [list(row)[::-1] for row in zip(*matrix)]
    for i in range(len(copy_matrix)):
        copy_matrix[i] = copy_matrix[i][::-1]

    return copy_matrix

def solution(scores):
    scores = rotate(scores)
    answer = ''
    for i in range(len(scores)):
        temp = 0
        count = 0
        for j in range(len(scores[i])):
            if i == j:
                if scores[i].count(scores[i][j]) == 1 and (min(scores[i]) == scores[i][j] or max(scores[i]) == scores[i][j]):
                    continue
                else:
                    temp += scores[i][j]
                    count += 1
            else:
                temp += scores[i][j]
                count += 1

        if 90 <= temp/count:
            answer += 'A'
        elif 80 <= temp/count < 90:
            answer += 'B'
        elif 70 <= temp/count < 80:
            answer += 'C'
        elif 50 <= temp/count < 70:
            answer += 'D' 
        else:
            answer += 'F'

    return answer

