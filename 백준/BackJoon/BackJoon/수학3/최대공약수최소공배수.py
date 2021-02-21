# a와 b의 최대공약수 G는 b와 a%b(a를 b로 나눈 나머지)의 최대공약수 G'과 서로 같다!
# 최소공배수는 바로 구할 수 있다. 여기서 두 수 A와 B가 있다고 할 때, A와 B는 각각 x*gcd(a, b), y*gcd(a, b)이다. 따라서 A*B/gcd(a, b)를 해주면 최소공배수가 된다

A, B = map(int, input().split())
a, b =  A, B

while b != 0 :
    a = a % b
    a, b = b, a

print(a)
print((A*B)//a)