def solution(A):
    # pair[i] = i, i+1을 덮는 타일의 합
    pair = [A[i] + A[i + 1] for i in range(len(A) - 1)]
    m = len(pair)

    if m == 0:
        return 0

    # dp[k][i]:
    # pair[0..i]까지 고려했을 때,
    # 타일을 최대 k개 사용해서 만들 수 있는 최대 합
    dp = [[0] * m for _ in range(4)]

    for k in range(1, 4): # 타일 개수 1, 2, 3
        for i in range(m): # pair의 인덱스
            # 1. 현재 타일 i를 사용하지 않는 경우
            skip = dp[k][i - 1] if i > 0 else 0

            # 2. 현재 타일 i를 사용하는 경우
            use = pair[i]
            # i를 쓰면 i+1 숫자까지 덮으므로,
            # 바로 이전 타일 i-1은 겹쳐서 사용할 수 없음
            if i >= 2:
                use += dp[k - 1][i - 2]

            dp[k][i] = max(skip, use)

    return dp[3][m - 1]

# 각 문제에서 주어진 숫자의 최소 최대 체크하고
# 1번 만족하는 쌍이 아예 없을 때 만족할 때 자리수 한개인경우 중복되는 숫자 있을 때 
# 2번 배열이 모두 같은 수로 되있을 때 
# 3번 배열의 길이 2 일때 1 일때 3일때 같은 숫자의 배열에따라 달라지는 값