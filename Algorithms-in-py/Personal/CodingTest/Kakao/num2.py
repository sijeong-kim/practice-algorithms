import math

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    string = ''
    while (n > 0):
        string = str(n % k) + string
        n //= k
    
    # print(string)

    answer = 0
    for i in string.split('0'):
        if i == '':
            continue
        else:
            if isPrime(int(i)):
                answer += 1

    # numbers = list(map(int, string.split('0')))
    # print(numbers)
    
    # answer = sum(list(map(isPrime, numbers)))

    return answer

print(solution(110011, 10))