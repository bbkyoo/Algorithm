https://velog.io/@timointhebush/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8B%A8%EC%96%B4-%EB%B3%80%ED%99%98-DFS-BFS-Python

def solution(begin, target, words):
    answer = 0
    q = [begin]
    while True:
        tmp_q = []
        for word_1 in q:
            if word_1 == target:
                return answer
            for word_2_idx in range(len(words)-1, -1, -1):
                word_2 = words[word_2_idx]
                difference = sum([x != y for x, y in zip(word_1, word_2)])
                if difference == 1:
                    tmp_q.append(words.pop(word_2_idx))
        if not tmp_q:
            return 0
        q = tmp_q
        answer += 1

