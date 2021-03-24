def dfs(idx, cnt):
    global answer

    if cnt == k - 5:
        read_cnt = 0
        for word in words:
            for w in word:
                if not visited[ord(w) - ord('a')]:
                    break
            else:
                read_cnt += 1

        answer = max(answer, read_cnt) if answer else read_cnt
        return

    for i in range(idx, 26):
        if not visited[i]:
            visited[i] = 1
            dfs(i, cnt + 1)
            visited[i] = 0

answer = None

n, k = map(int, input().split())

words = []

for _ in range(n):
    s = set(input())
    words.append(s)

if k < 5:
    print(0)
    exit(0)

elif k == 26:
    print(len(words))
    exit(0)
                
visited = [0] * 26

for i in ('a','c','i','n','t'):
    visited[ord(i) - ord('a')] = 1

dfs(0,0)
print(answer)






















