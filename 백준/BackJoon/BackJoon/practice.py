import sys

input = sys.stdin.readline

n, clock = input().rstrip().split()

nums = []
for _ in range(int(n)):
    nums.append(input().rstrip())

clock = list(map(int,clock.split(":")))

count = 0
idx = 0
for i in range(int(n)-1,-1,-1):
    nums[i] = list(map(int,nums[i].split(":")))

    if clock[0] == 0:
        temp = [0,0]
        cnt = 0
        for j in range(i, int(n)):
            temp[1] += nums[j][1]
            temp[0] += nums[j][0]
            if temp[1] >= 60:
                temp[1] -= 60
                temp[0] += 1

            if (temp[0] > clock[1]):
                cnt += 1
                break
            elif temp[0] == clock[1] and temp[1] >= clock[2]:
                cnt += 1
                break

            cnt += 1
    
        if count <= cnt:
            count = cnt
            idx = i
    else:
        temp = [0,0,0]
        cnt = 0
        for j in range(i, int(n)):
            temp[2] += nums[j][1]
            temp[1] += nums[j][0]

            if temp[2] >= 60:
                temp[2] -= 60
                temp[1] += 1

            if temp[1] >= 60:
                temp[1] -= 60
                temp[0] += 1

            if (temp[0] > clock[0]):
                cnt += 1
                break
            elif temp[0] == clock[0] and temp[1] >= clock[1]:
                cnt += 1
                break
            elif temp[0] == clock[0] and temp[1] == clock[1] and temp[0] >= clock[0]:
                cnt += 1
                break

            cnt += 1
    
        if count <= cnt:
            count = cnt
            idx = i

print(count, idx+1)



