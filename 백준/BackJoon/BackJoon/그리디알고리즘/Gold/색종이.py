import sys
input = sys.stdin.readline

nums = []
for i in range(6):
    nums.append(int(input()))

result = nums.pop()
nums.reverse()

for i in range(len(nums)):
    if nums[i] == 0:
        continue

    if i == 0:
        while nums[i]:
            if nums[4] >= 11:
                nums[4] -= 11
                nums[i] -= 1
            else:
                nums[4] = 0
                nums[i] -= 1
            result += 1

    elif i == 1:
        while nums[i]:
            if nums[3] >= 5:
                nums[3] -= 5
                nums[i] -= 1
            else:
                nums[i] -= 1
                if nums[4] >= 20 - (4 * nums[3]):
                    nums[4] -= 20 - (4 * nums[3])
                else:
                    nums[4] = 0
                nums[3] = 0
            result += 1

    elif i == 2:
        while nums[i]:
            if nums[i] >= 4:
                result += nums[i]//4
                nums[i] %= 4
            else:
                init = 36
                init -= 9*nums[i]
                nums[i] = 0
                nums[3] -= init//4
                init %= 4

                if init:
                    if nums[4] >= init:
                        nums[4] -= init
                    else:
                        nums[4] = 0
                result += 1

    elif i == 3:
        while nums[i]:
            if nums[i] >= 9:
                result += nums[i]//9
                nums[i] %= 9
            else:
                init = 36
                init -= nums[i]*4
                if init:
                    if nums[4] >= init:
                        nums[4] -= init
                    else:
                        nums[4] = 0
                result += 1

    else:
        result += nums[i]//36
        if nums[i]%36 != 0:
            result += 1

print(result)