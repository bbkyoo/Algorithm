#https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A9%80%EC%A9%A1%ED%95%9C-%EC%82%AC%EA%B0%81%ED%98%95-in-python
# (가로 * 세로) - (가로 + 세로 - (가로세로의)최대공약수) 
import math

def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))

