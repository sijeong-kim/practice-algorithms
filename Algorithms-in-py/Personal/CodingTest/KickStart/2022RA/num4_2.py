import sys, math
input = sys.stdin.readline

def is_prime():
    primes = [-1, -1] + [0] * (MAX-1)
    for i in range(2, int(math.sqrt(MAX-1))):
        if primes[i] == 0:
            for j in range(i*i, MAX+1, i):
                primes[j] = i
    return primes

def add_primes(factorized, num):
    if num == 1:
        return
    while primes[num]:
        factorized[primes[num]] += 1
        num //= primes[num]    
    factorized[num] += 1

def sub_primes(factorized, num):
    if num == 1:
        return
    while primes[num]:
        factorized[primes[num]] -= 1
        num //= primes[num]    
    factorized[num] -= 1

def solution(a, b):
    ans = 0
    
    for num in range(a, b+1):
        isInter = True
        zero_check = False
        digits = list(map(int, str(num)))
        
        factorized = [0] * (MAX+1)
        for i in range(len(digits)):
            if digits[i] == 0:
                # print(f"{num}: 0이 있음")
                ans += 1
                zero_check = True
                break
            add_primes(factorized, digits[i])
        
        if zero_check:
            continue
        
        sub_primes(factorized, sum(digits))

        for cnt in factorized:
            if cnt < 0:
                isInter = False
                # print(f"{num}: 나눠지지 않음")

        if isInter: 
            ans += 1
            # print(f"{num}: 해당")
            
    return ans
        
if __name__ == "__main__":
    t = int(input())
    MAX = 13 * 9 + 1
    
    primes = is_prime()
    for case in range(1, t+1):
        a, b = map(int, input().split())
        ans = solution(a, b)
        print(f"Case #{case}: {ans}")
        
    