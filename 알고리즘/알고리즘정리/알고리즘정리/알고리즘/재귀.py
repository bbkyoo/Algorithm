import random

# 1. 재귀
# 함수 안에서 자기 자신을 호출하는 형태

# 2. 재귀 호출의 일반적인 형태

# 일반적인 형태1
# def function(입력):
#     if 입력 > 일정값:
#         return function(입력 - 1)
#     else:
#         return 일정값

# 시간 복잡도/ 공간 복잡도 둘 다 O(n)
def factorial(num):
    if num <= 1:
        return num
    else:
        return num * factorial(num-1) 

# 일반적인 형태2
# def function(입력):
#     if 입력 <= 일정값:
#         return 일정값, 입력값, 또는 특정값
#     function(입력값보다 작은값)
#     return 결과값

def factorial(num):
    if num <= 1:
        return num
    return_value = num * factorial(num-1)
    return return_value

# 파이썬에서는 재귀 함수는 깊이가 1000회 이하가 되어야 함

# 3. 재귀 용법을 활용한 프로그래밍 연습

# 다음 함수를 재귀함수를 활용해서 1부터 num까지의 곱이 출력되게 만드세요
def multiple(num):
    if num <= 1:
        return num
    else:
        return num * multiple(num-1)

# 숫자가 들어 있는 리스트가 주어졌을때 리스트의 합을 리턴하는 함수를 만드세요

def sum_list(data):
    if len(data) <= 1:
        return data[0]
    else:
        return data[0] + sum_list(data[1:]) 
    
# 회문은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 의미함
# 회문을 판별할 수 있는 함수를 리스트 슬라이싱을 활용해서 만드세요 

def palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False

# 1. 정수 n에 대해 
# 2. n이 홀수이면 3 X n+1 을 하고
# 3. n이 짝수이면 n 을 2로 나누어서
# 4. n이 1이 될떄까지 2 와 3의 과정을 반복

def func(n):
    if n <= 1:
        return n 

    if n % 2 == 1:
        return(func((3*n)+1))
    else:
        return(func(int(n/2)))
        
# 정수 n을 1, 2, 3의 합으로 나타낼 수 있는 방법의 수를 구하시오.

def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        func(n-1) + func(n-2) + func(n-3) 







