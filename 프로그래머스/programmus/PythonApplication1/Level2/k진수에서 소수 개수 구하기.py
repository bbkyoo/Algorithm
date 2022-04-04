def solution(n, k):
    def isPrime(num):
        if num == 1:
            return False

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    nums = []
    while n != 0:
        nums.append(str(n % k))
        n //= k
    s = "".join(reversed(nums)).split('0')

    cnt = 0
    for i in s:
        if len(i) != 0 and isPrime(int(i)):
            cnt += 1
    return cnt
