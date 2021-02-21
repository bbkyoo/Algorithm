def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            else:
                if (numbers[i] + numbers[j]) in answer:
                    continue
                else:
                    answer.append(numbers[i] + numbers[j])
    answer.sort()
    return answer

num = [5,0,2,7]

print(solution(num))