def solution(price):
    answer = [0] * len(price)

    for i in range(len(price)-1):
        for j in range(i, len(price)-1):
                if price[i] > price[j]: 
                    break
                else:
                    answer[i] += 1

    return answer

print(solution([1,2,3,2,3]))