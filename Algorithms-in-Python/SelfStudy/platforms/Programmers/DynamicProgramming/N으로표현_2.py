
def solution(N, number):
    # N: 1 이상 9 이하
    # number 만들고자 하는 숫자

    if number == N:
        return 1

    dp = [set() for _ in range(9)] # i 번 사용한 결과

    dp[1].add(N)

    for i in range(1, 9): # i 번 사용한 결과
        # 이어 붙이기
        dp[i].add(int(str(N) * i))

        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i-j]:
                    # 사칙 연산
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)

        if number in dp[i]:
            return i

    return -1


if __name__ == "__main__":
    # N = 5
    # number = 12
    N = 2
    number = 11
    answer = solution(N, number)
    print(answer)
