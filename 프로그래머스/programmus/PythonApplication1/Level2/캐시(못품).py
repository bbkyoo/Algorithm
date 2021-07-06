#LRU(Least Recently Used) 알고리즘에 대해서 알아야 합니다. 캐시의 사이즈는 한정 되어있기 때문에 
#캐시 사이즈가 꽉 찬 상태에서 새로운 캐시를 넣으려면 기존 캐시에 있던 데이터를 교체해야하는 데 
#여기서 어떤 데이터를 교체할 것인가가 캐시 교체 알고리즘의 목적

from collections import deque

def solution(cacheSize, cities):
    cache = deque()
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5
    else:
        for i in cities:
            i = i.lower()
            if i in cache:
                answer += 1
            else:
                answer += 5

            if i in cache:  # 여기 우선 순위 높이는 방법 주목 이걸 걍 지우고
                cache.remove(i)
            else:
                if len(cache) >= cacheSize:
                    cache.popleft()

            cache.append(i) # 맨 뒤에 첨가만 해주면 됨

    return answer









