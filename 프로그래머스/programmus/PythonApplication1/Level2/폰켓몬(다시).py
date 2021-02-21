def solution(nums):
    answer = 0
    length = len(nums) // 2
    nums.sort()
    last = 0

    for i in nums:
        if i != last and answer < length:
            answer += 1
            last = i

    return answer

