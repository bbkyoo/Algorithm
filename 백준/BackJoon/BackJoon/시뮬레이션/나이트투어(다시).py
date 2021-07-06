arr = [input() for _ in range(36)]

if len(set(arr)) == 36:
    for i in range(35):
        if abs((ord(arr[i][0]) - ord(arr[i+1][0])) * (int(arr[i][1]) - int(arr[i+1][1]))) != 2:
            print("Invalid")
            break

    else:
        for a, b in [[-2, -1], [-2, 1], [-1, -2], [1,-2], [2, -1], [2, 1], [1, 2], [-1, 2]]:
            c = ord(arr[-1][0]) + a
            n = int(arr[-1][1]) + b
            if ord('A') <= c <= ord('Z') and 1 <= n <= 6:
                if chr(c) == arr[0][0] and n == int(arr[0][1]):
                    print('Valid')
                    break

        else:
            print('Invalid')
else:
    print('Invalid')