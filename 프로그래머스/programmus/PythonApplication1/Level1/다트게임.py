def solution(dartResult):
    arr = []

    for i in range(len(dartResult)):
        if dartResult[i] == "S" or dartResult[i] == "D" or dartResult[i] == "T":
            if dartResult[i-2:i] == "10":
                arr.append(dartResult[i-2:i+1])
            else:
                arr.append(dartResult[i-1:i+1])
        elif dartResult[i] == "*" or dartResult[i] == "#":
            arr.append(dartResult[i])

    result = []
    for i in range(len(arr)):
        if "S" in arr[i]:
            if "10" in arr[i]:
                result.append(int(arr[i][0:2]))
            else:
                result.append(int(arr[i][0]))
        elif "D" in arr[i]:
            if "10" in arr[i]:
                result.append(int(arr[i][0:2])**2)
            else:
                result.append(int(arr[i][0])**2)
        elif "T" in arr[i]:
            if "10" in arr[i]:
                result.append(int(arr[i][0:2])**3)
            else:
                result.append(int(arr[i][0])**3)
        else:
            result.append(arr[i])

    for i in range(len(result)):
        if result[i] == "*":
            if i == 1:
                result[i-1] = result[i-1] * 2        
            elif i == 2:
                result[i-1] = result[i-1] * 2
                result[i-2] = result[i-2] * 2
            elif i == 3:
                if result[1] == "*" or result[1] == "#":
                    result[i-1] = result[i-1] * 2
                    result[i-3] = result[i-3] * 2
                else:
                    result[i-1] = result[i-1] * 2
                    result[i-2] = result[i-2] * 2
            elif i == 4:
                if result[1] == "*" or result[1] == "#":
                    result[i-1] = result[i-1] * 2
                    result[i-2] = result[i-2] * 2
                elif result[2] == "*" or result[2] == "#":
                    result[i-1] = result[i-1] * 2
                    result[i-3] = result[i-3] * 2
            elif i == 5:
                result[i-1] = result[i-1] * 2
                result[i-3] = result[i-3] * 2
        elif result[i] == "#":
            result[i-1] = result[i-1] * (-1)

    answer = 0

    for i in range(len(result)):
        if result[i] != "*" and result[i] != "#":
            answer += result[i]

    return answer

        








