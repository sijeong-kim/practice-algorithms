def solution(n, times):
    answer = 0
    
    # 입국심사를 기다리는 사람 수 N
    # 각 심사관이 한 명을 심사하는데 걸리는 시간 배열
    # 심사를 받는데 걸리는 시간 최소값
    
    def is_possible(total_time):
        people = 0
        for t in times:
            people += total_time // t

        if people < n:
            return False
        else:
            return True

    left = 0
    right = max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        
        if is_possible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
                    
    return answer