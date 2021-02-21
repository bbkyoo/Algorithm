#N*N*N의 주사위 더미를 가정해보자.
#밑면과 옆면, 윗면으로 나누어서 풀 수 있다.
#밑면은 변과 꼭지점을 가지고
#옆면과 윗면은 변과 꼭지점과 중앙의 (N-2)^2의 면을 가진다.
#또한 주사위가 돌출되는 부분의 최솟값을 먼저 구해주는 게 중요하다.
#윗면의 꼭지점이 3면이 돌출되고, 나머지면은 2면 혹은 1면만 돌출된다.

#1면 최솟값은 6개의 면 중 가장 작은 값을
#2면 최솟값은 반대면을 제외한 두 값을 합친 것 중 가장 작은 값을
#3면 최솟값은 A/F * B/E * C/D 조합으로 총 8가지의 경우의 수가 나온다.

N = int(input())

dice = list(map(int, input().split()))

# A, B, C, D, E, F
# 0, 1, 2, 3, 4, 5
# i + j == 5 -> 반대편

if N == 1:
    print(sum(dice) - max(dice))
else:
    # 1면 최솟값
    min_one = min(dice)

    # 2면 최솟값
    min_two = sum(dice)
    for i in range(6):
        for j in range(6):
            if i != j and i + j != 5: # 반대편
                min_two = min(min_two, dice[i] + dice[j])

    # 3면 최솟값 --> 이 부분을 잘 기억
    min_three = sum(dice)
    for i in [0, 5]:
        for j in [1, 4]:
            for k in [2,3]:
                min_three = min(min_three, dice[i] + dice[j] + dice[k])

    # 밑면
    base_side = 0
    # 밑면 꼭지점
    base_side += min_two * 4
    # 밑면 변
    base_side += min_one * 4 * (N-2)
    # 윗면
    upper_side = 0
    # 윗면 꼭지점
    upper_side += min_three * 4
    # 윗면 변
    upper_side += min_two * 4 * (N-2)
    # 윗면 중앙면
    upper_side += min_one * ((N-2)**2)
    # 옆면
    side = 0
    # 옆면 꼭지점
    side += min_two * 4 * (N-2)
    # 옆면 중앙면
    side += min_one * 4 * ((N-2)**2)

    print(upper_side + side + base_side)

























