
def calculate_danger_btw_closest(x, idx, supply):
    if idx == 0:
        arr = [abs(a - x) for a in supply[idx:idx + 3]]
    elif idx == n-2:
        arr = [abs(a - x) for a in supply[idx - 1:idx + 2]]
    elif idx == n-1:
        arr = [abs(a - x) for a in supply[idx - 1:idx + 1]]
    else:
        arr = [abs(a - x) for a in supply[idx-1:idx+3]]

    arr.sort()
    return max(arr[0], arr[1])


def solution(n, supply):
    supply.sort()
    answer = 0
    left = supply[0]
    right = supply[-1]
    idx = 0
    for x in range(left, right+1): # x가 right인 경우
        if supply[idx+1] == x: # idx = n-1
            idx += 1

        # 가장 가까운 점을 찾기
        # if idx == 0 or idx == n-2: 예외 처리
        danger = calculate_danger_btw_closest(x, idx, supply)
        if danger > answer:
            answer = danger
    return answer
