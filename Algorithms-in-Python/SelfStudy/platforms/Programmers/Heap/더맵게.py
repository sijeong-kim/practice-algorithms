def solution(scoville, K):
    answer = 0
    # 모든 음식의 스코빌 지수를 K이상으로 만들기 위해
    # 가장 맵지 않은 음식의 스코빌 지수 + 두 번째로 맵지 않은 음식의 스코빌 지수 * 2
    # 최소 힙
    import heapq
    
    heapq.heapify(scoville) # 최소힙
    
    while scoville and scoville[0] < K: # 최소값이 K 미만인 경우 계속 썪기
        if len(scoville) == 1: # 한 개인데도 K 미만인 경우 붊가능
            return -1 
        min_val = heapq.heappop(scoville) # 최소값
        min_val_2 = heapq.heappop(scoville) # 두번째 최소값

        heapq.heappush(scoville, min_val + min_val_2 * 2)
        answer += 1
    
    # 최소값이 K 이상인 경우 가능
    # 섞는 최소 횟수
    return answer