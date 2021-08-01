# 파이썬의 내장 모듈인 collections의 defaultdict 클래스를 사용해 기본값을 넣어주면 된다. 
# defaultdict 클래스의 생성자로 기본값을 생성해주는 함수를 넘기면, 모든 키에 대해서 값이
# 없는 경우 자동으로 생성자의 인자로 넘어온 함수를 호출하여 그 결과값으로 설정해준다.

# 정말 중요한점!! dic는 sort는 안먹어도 sorted로 해결이 가능하다.

from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_dic = defaultdict(lambda: 0) # 이 부분 아주 중요 dic는 꼭 이렇게 선언 
    total_list = defaultdict(lambda: []) # 이 부분 아주 중요 dic에 리스트값을 append하고 싶으면 꼭 이렇게

    for i in range(len(genres)):
        genre_dic[genres[i]] += plays[i] # 이렇게 넣어주는 것도 외우기
        total_list[genres[i]].append((plays[i], i)) # 이렇게 넣어주는 것도 외우기

    genre_dic = sorted(genre_dic.items(), key=lambda x:x[1], reverse=True) # 이 부분 아주 중요 이렇게 함으로써 genre_dic는 리스트로 변경 됨 한마디로 dic가 리스트로 변경하게 하는 방법임
    
    for i in total_list:
        total_list[i] = sorted(total_list[i], key=lambda x:x[0], reverse=True) # 이 부분 아주 중요
   
    while len(genre_dic) > 0:
        genre_max = genre_dic.pop(0)
        for t in total_list:
            if t == genre_max[0]:
                if len(total_list[t]) > 1:
                    answer.append(total_list[t][0][1])
                    answer.append(total_list[t][1][1])
                else:
                    answer.append(total_list[t][0][1])

    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
