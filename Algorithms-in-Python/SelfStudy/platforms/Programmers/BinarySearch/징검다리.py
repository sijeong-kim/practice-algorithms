def solution(distance, rocks, n):
    # 각 지점 사이 최소값 중 가장 큰 값

    # 출발지점부터 도착지점까지의 거리 distance
    # 바위들이 있는 위치를 담은 배열 rocks
    # 제거할 바위의 수 n

    # dist 가 최소 값이 되도록 판별
    # dist 이상 간격이 되도록 바위를 제거
    # 바위가 n개 초과하여 제거 되면 False
    # 아니면 True

    rocks.sort()
    rocks.append(distance)

    # [0, 2, 11, 14, 17, 21, 25]
    def is_possible(min_dist):
        cnt = n # remove 남은 횟수

        now = 0
        for i in range(len(rocks)):
            if min_dist > rocks[i] - now:
                cnt -= 1
                if cnt < 0:
                    return False
            else:
                now = rocks[i]

        return True

    left = 1
    right = distance

    while left <= right:
        mid = (left + right) // 2

        if is_possible(mid):
            left = mid + 1
        else:
            right = mid - 1

    return right

if __name__ == "__main__":
    distance = 25
    rocks = [2, 14, 11, 21, 17]
    n = 2

    answer = solution(distance, rocks, n)
    print(answer)