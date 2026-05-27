# 위험도: 두번째로 가까운 보급 창고의 거리
def calculate_danger(x, supply):
    dist = sorted([abs(s - x) for s in supply])
    return max(dist[0], dist[1])


# 가장 위험도가 큰 위치, 그때의 위험도 -> 이분 탐색
def solution(n, supply):
    # n: 보급 창고 개수
    # supply: 보급 창고 위치 (짝수, 중복 X), 가장 가까운 보급 창고로부터 물품을 지원 받음
    supply.sort() # 오름차순 정렬
    answer = 0
    left = supply[0]
    right = supply[-1]
    for x in range(left, right+1):
        danger = calculate_danger(x, supply)
        if answer < danger:
            answer = danger

    return answer
