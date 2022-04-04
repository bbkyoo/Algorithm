def solution(numbers):
    arr = []
    for i in range(10):
        arr.append(i)

    for i in numbers:
        if i in arr:
            arr.remove(i)

    return sum(arr)