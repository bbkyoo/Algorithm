# 왼손 시작은 *, 오른 손 시작은 #
# 1, 4, 7 을 누를 때는 왼손
# 3, 6, 9 를 누를 때는 오른손
# 2,5,8,0 을 누를 때는 두 엄지손가락에서 더 가까운 거리에서 사용, 만약 거리가 같다면 손잡이의 방향을 보고 누른다.

def solution(numbers, hand):
    arr = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    answer = ''
    left = [[3,0]]
    right = [[3,2]]
    k = 0
    while k < len(numbers): 
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == numbers[k]:
                    if numbers[k] == 1 or numbers[k] == 4 or numbers[k] == 7:
                        left.pop()
                        left.append([i,j])
                        answer += 'L'
                    elif numbers[k] == 3 or numbers[k] == 6 or numbers[k] == 9:
                        right.pop()
                        right.append([i,j])
                        answer += 'R'
                    elif numbers[k] == 2 or numbers[k] == 5 or numbers[k] == 8 or numbers[k] == 0:
                        if k == 0:
                            if hand == "right":
                                right.pop()
                                right.append([i,j])
                                answer += 'R'
                            else:
                                left.pop()
                                left.append([i,j])
                                answer += 'L'
                        else:
                            if (abs(i - left[0][0]) + abs(j - left[0][1])) < (abs(i - right[0][0]) + abs(j - right[0][1])):
                                left.pop()
                                left.append([i,j])
                                answer += 'L'
                            elif (abs(i - left[0][0]) + abs(j - left[0][1])) > (abs(i - right[0][0]) + abs(j - right[0][1])):
                                right.pop()
                                right.append([i,j])
                                answer += 'R'
                            else:
                                if hand =="right":
                                    right.pop()
                                    right.append([i,j])
                                    answer += 'R'
                                else:
                                    left.pop()
                                    left.append([i,j])
                                    answer += 'L'
        k += 1
    return answer






