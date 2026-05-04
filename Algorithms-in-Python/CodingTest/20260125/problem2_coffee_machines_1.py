import heapq

def solution(n, coffee_times):
    # 커피 추출구 개수 N
    # 커피 만드는데 걸리는 시간이 주문번호 순서대로 담긴 배열 coffee_times
    
    # return 커피가 완성되는 순서대로 주문번호를 담은 배열
    
    m = len(coffee_times)
    q = [(coffee_times[i], i) for i in range(n)] # n개 만큼 만들기 시작
    next_index = n
    
    answer = []
    heapq.heapify(q)
    print(f"q: {q}")
    
    while q: # O(M)
        
        # 시간이 가장 적게 걸리는 커피 pop
        curr_time, curr_index = heapq.heappop(q) 
        print(f"curr: {curr_time, curr_index}")
        
        # 완성된 커피 번호 업데이트
        answer.append(curr_index+1)
        
        # 나머지 커피들 시간 업데이트       
        q = [(rest_time-curr_time, rest_index) for rest_time, rest_index in q] # O(N)

        # 다음 커피 우선순위 큐에 추가
        if next_index < m:
            heapq.heappush(q, (coffee_times[next_index], next_index))
            next_index += 1
            
        print(f"q: {q}")
            
    
    
    return answer


n = 3
coffee_times = [3, 2, 1, 1]
answer = solution(n, coffee_times)

print(answer)

        

        