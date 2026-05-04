
def solution(N, number):
    # N, number
    # concate, /, +, *, - 
    # 5 ** 8 = 625 * 625
    # 8보다 커지면 return -1하기
    
    answer = 0
    dp = [set() for i in range(9)] # i 번 사용했을 때 만들어지는 값 저장
    
    for i in range(1, 9):
        dp[i].append(int(str(N)*i)) # 이어붙인 수
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[j].add(a + b)
                    dp[j].add(a - b)
                    dp[j].add(a * b)
                
                    if b != 0:
                        dp[j].add(a // b)


        if number in dp[i]:
            return i
    return -1
    # N과 사칙연산만 사용해서 표현할 수 있는 방법 중
    # N 사용횟수의 최소값을 return
    # 최소값이 8보다 크면 -1 return
    

# 다시 풀기