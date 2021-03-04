# 정규식을 잘 알아두기 
# 정규식 https://wikidocs.net/4308
# [a-zA-Z] : 알파벳 모두
# [0-9] : 숫자

import re

def solution(files):
    temp = [re.split(r"([0-9]+)", s) for s in files]
    
    sort = sorted(temp, key = lambda x:(x[0].lower(), int(x[1])))
    
    return ["".join(s) for s in sort]
