import sys, math
input = sys.stdin.readline

def is_prime():
    primes = [-1, -1] + [0] * (MAX-1)
    for i in range(2, int(math.sqrt(MAX))):
        if primes[i] == 0:
            for j in range(i*i, MAX+1, i):
                primes[j] = i
    return primes

def add_primes(num):
    if num == 1:
        return
    while primes[num]:
        factorized[primes[num]] += 1
        num //= primes[num]    
    factorized[num] += 1

def sub_primes(num):
    if num == 1:
        return
    while primes[num]:
        factorized[primes[num]] -= 1
        num //= primes[num]
    factorized[num] -= 1

def solution(a, b):
    global factorized

    
    ans = 0
    for n in range(a, b+1):
        factorized = [0 for _ in range(MAX+1)]   
        digits = list(map(int, str(n)))
            
        isInteresting = True
        
        # product
        for d in digits:
            add_primes(d)
        
        # sum
        sum_digits = sum(digits)
        
        # divide
        sub_primes(sum_digits)
        
        for cnt in factorized:
            if cnt < 0:
                isInteresting = False
                break
        
        if isInteresting: cnt += 1

    return ans

if __name__ == "__main__":
    MAX = int(1e9)
    primes = is_prime()
    t = int(input())
    factorized = []
    for case in range(1, t+1):
        a, b = map(int, input().split())
        ans = solution(a, b)
        print(f"Case #{case}: {ans}")
        
    