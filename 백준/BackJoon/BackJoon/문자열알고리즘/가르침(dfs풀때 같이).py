#언어는"anta"로 시작되고, "tica"로 끝나므로 배울 수 있는 단어 중, 'a', 'c', 'i', 'n', 't'를 배워야 하므로 5를 제외한다.
#만약 K가 5보다 작다면, 읽을 수 있는 단어는 없다.
#K가 26이라면 모든 알파벳을 배울 수 있으므로 주어진 단어 N을 다 읽을 수 있다.
#DFS는 백트랙킹을 통해, a ~ z 중 K - 5 만큼 배운 후 몇 개의 단어를 읽을 수 있는지 확인한다.

def dfs(idx, cnt):
    global answer

    if cnt == k - 5:
        read_cnt = 0
        for word in words:
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    break
            else:
                read_cnt += 1
        answer = max(answer, read_cnt) if answer else read_cnt
        return
    
    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False

answer = None
n, k = map(int, input().split())

if k < 5 or k == 26:
    print(0 if k < 5 else n)
    exit(0)

words = [set(input().rstrip()) for _ in range(n)]
learn = [False]  * 26

for c in ('a','c','i','n','t'):
    learn[ord(c) - ord('a')] = True # ord(c)는 문자의 아스키 코드 값을 돌려주는 함수

dfs(0, 0)
print(answer)















