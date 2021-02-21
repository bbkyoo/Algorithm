# [0, 트럭] -> [트럭,0]-> [0,0] 이런식으로 트럭이 들어오고 나가게 구현 함으로써 해결할 수 있었다.
# 전형적인 큐에 관한 문제 (먼저 들어온 것은 먼저 나간다.)

def solution(bridge_length, weight, truck_weights):
    time = 0
    q = [0] * bridge_length

    while q:
        time += 1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return time










