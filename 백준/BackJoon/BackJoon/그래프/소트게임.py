from collections import deque

n, k = map(int, input().split())
arr = list(input().split())

visited = set("".join(arr))
q = deque([["".join(arr), 0]])

ans = -1

while q:
    word, cnt = q.popleft()
    temp = list(word)

    if temp == sorted(arr):
        ans = cnt
        break

    isFirst = False

    for i in range(n-k+1):
        new = list(temp)
        target = new[i:i+k]
        target.reverse()
        for j in range(k):    
            new[i+j] = target[j]

        newWord = "".join(new)
        if newWord not in visited:
            visited.add(newWord)
            q.append([newWord, cnt+1])

print(ans)





