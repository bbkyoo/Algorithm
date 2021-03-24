king, rock, n = input().split()

for i in range(int(n)):
    move = input()

    if move == 'R':
        if ord('A') <= ord(king[0]) + 1 <= ord('H') and 1 <= int(king[1]) <= 8:
            king = chr(ord(king[0])+1) + king[1]

            if king == rock:
                if ord('A') <= ord(rock[0]) + 1 <= ord('H') and 1 <= int(rock[1]) <= 8:
                    rock = chr(ord(rock[0])+1) + rock[1]

                else:
                    continue
        else:
            continue

    elif move == 'L':
        if ord('A') <= ord(king[0]) - 1 <= ord('H') and 1 <= int(king[1]) <= 8:
            king = chr(ord(king[0])-1) + king[1]

            if king == rock:
                if ord('A') <= ord(rock[0]) - 1 <= ord('H') and 1 <= int(rock[1]) <= 8:
                    rock = chr(ord(rock[0])-1) + rock[1]
                else:
                    continue
        else:
            continue

    elif move == 'B':
        if ord('A') <= ord(king[0]) <= ord('H') and 1 <= int(king[1]) - 1 <= 8:
            king = king[0] + str(int(king[1]) - 1)

            if king == rock:
                if ord('A') <= ord(rock[0]) <= ord('H') and 1 <= int(rock[1]) - 1 <= 8:
                    rock = rock[0] + str(int(rock[1]) - 1)

                else:
                    continue

        else:
            continue


    elif move == 'T':
        if ord('A') <= ord(king[0]) <= ord('H') and 1 <= int(king[1]) + 1 <= 8:
            king = king[0] + str(int(king[1]) + 1)

            if king == rock:
                if ord('A') <= ord(rock[0]) <= ord('H') and 1 <= int(rock[1]) + 1 <= 8:
                    rock = rock[0] + str(int(rock[1]) + 1)
                else:
                    continue

        else:
            continue
        

    elif move == 'RT':
        if ord('A') <= ord(king[0]) + 1 <= ord('H') and 1 <= int(king[1]) + 1 <= 8:
            king = chr(ord(king[0]) + 1) + str(int(king[1]) + 1)

            if king == rock:
                if ord('A') <= ord(rock[0] + 1) <= ord('H') and 1 <= int(rock[1]) + 1 <= 8:
                    rock = chr(ord(rock[0]) + 1) + str(int(rock[1]) + 1)

                else:
                    continue
        else:
            continue

    elif move == 'LT':
        if ord('A') <= ord(king[0]) - 1 <= ord('H') and 1 <= int(king[1]) + 1 <= 8:
            king = chr(ord(king[0]) - 1) + str(int(king[1]) + 1)

            if king == rock:
                if ord('A') <= ord(rock[0] - 1) <= ord('H') and 1 <= int(rock[1]) + 1 <= 8:
                    rock = chr(ord(rock[0]) - 1) + str(int(rock[1]) + 1)

                else:
                    continue

        else:
            continue

    elif move == 'RB':
        if ord('A') <= ord(king[0]) + 1 <= ord('H') and 1 <= int(king[1]) - 1 <= 8:
            king = chr(ord(king[0]) + 1) + str(int(king[1]) - 1)

            if king == rock:
                if ord('A') <= ord(rock[0] + 1) <= ord('H') and 1 <= int(rock[1]) - 1 <= 8:
                    rock = chr(ord(rock[0]) + 1) + str(int(rock[1]) - 1)
                else:
                    continue
        
        else:
            continue

    elif move == 'LB':
        if ord('A') <= ord(king[0]) - 1 <= ord('H') and 1 <= int(king[1]) - 1 <= 8:
            king = chr(ord(king[0]) - 1) + str(int(king[1]) - 1)

            if king == rock:
                if ord('A') <= ord(rock[0] - 1) <= ord('H') and 1 <= int(rock[1]) - 1 <= 8:
                    rock = chr(ord(rock[0]) - 1) + str(int(rock[1]) - 1)
                else:
                    continue

        else:
            continue

print(king)
print(rock)







