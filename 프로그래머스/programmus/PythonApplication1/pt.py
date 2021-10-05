#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, price, cost):
        answer = 0
        result = 0
        
        for i in range(len(price)):
            temp = 0
            for j in range(len(cost)):
                if price[i] - cost[j] >= 0 and price[j] >= price[i]:
                    temp += price[i] - cost[j]
               
            if answer == temp and result >= price[i]:
                result = price[i]

            elif answer < temp:
                answer = temp
                result = price[i]

        return result
