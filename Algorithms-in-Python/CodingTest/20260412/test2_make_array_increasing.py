def solution(A):
    moves = 0

    # A[i] >= A[i + 1]인 경우,
    # A[i + 1]부터 시작하는 구간을 증가시키는 연산이 최소 1번 필요
    for i in range(len(A) - 1):
        if A[i] >= A[i + 1]:
            moves += 1
    
    return moves