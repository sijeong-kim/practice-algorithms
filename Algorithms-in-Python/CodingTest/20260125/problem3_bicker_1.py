from collections import deque

def solution(a, b, c, d):
    
    answer = 0
    
    # 초기 상태: 물이 모두 0인 상태, 이동 횟수 0
    q = deque([(0, 0, 0, 0)])
    visited = set([(0, 0, 0)])
    caps = [a, b, c] # 각 비커의 최대 용량
    
    while q:
        curr = q.popleft()
        states = list(curr[:3]) # 현재 비커 상태 (a, b, c)
        steps = curr[3]
        
        # 목표 달성 확인
        if d in states: return steps
        
        # 가능한 모든 행동 시뮬레이션
        next_states = []

        for i in range(3):
            # 1. 가득 채우기
            temp = states[:]
            temp[i] = caps[i]
            next_states.append(tuple(temp))
            
            # 2. 모두 버리기
            temp = states[:]
            temp[i] = 0
            next_states.append(tuple(temp))
            
            # 3. 비커끼리 옮기기 (i->j)
            for j in range(3):
                if i == j: continue
                
                temp = states[:]
                # 옮길 수 있는 양 = min(내 물의 양, 상대 비커의 남은 공간)
                move = min(states[i], caps[j]-states[j])
                temp[i] -= move
                temp[j] += move
                next_states.append(tuple(temp))                
                
        # 방문 안한 새로운 상태만 큐 추가
        for ns in next_states:
            if ns not in visited:
                visited.add(ns)
                q.append(ns + (steps + 1,))
                
                
    return -1 # 못 만들면 -1


a, b, c, d = 3, 5, 7, 1

answer = solution(a, b, c, d)

print(answer)
