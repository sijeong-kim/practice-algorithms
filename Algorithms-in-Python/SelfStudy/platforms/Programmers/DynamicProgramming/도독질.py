def solution(money):

    n = len(money)

    if n <= 3:
        return max(money)

    # case1: 0을 턴 경우 -> n-1 못텀
    dp_1 = [0] * n  # i 번까지 털었을 때 최대값
    dp_1[0] = money[0]
    dp_1[1] = money[0]
    for i in range(2, n-1):
        dp_1[i] = max(dp_1[i-2] + money[i], dp_1[i-1])
    dp_1[n-1] = dp_1[n-2]

    # case2: 0을 안 턴 경우 -> n-1 털 수 있음
    dp_2 = [0] * n
    dp_2[1] = money[1]
    for i in range(2, n):
        dp_2[i] = max(dp_2[i-2] + money[i], dp_2[i-1])

    return max(dp_1[n-1], dp_2[n-1])


if __name__ == "__main__":
    money = [1, 2, 3]
    answer = solution(money)
    print(answer)