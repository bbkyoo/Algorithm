# 최대공약수 구하기

from math import gcd
import sys

input = sys.stdin.readline

n, m = map(int, input().split(':'))

gd = gcd(n, m)
n //= gd
m //= gd

print("{}:{}".format(n, m))