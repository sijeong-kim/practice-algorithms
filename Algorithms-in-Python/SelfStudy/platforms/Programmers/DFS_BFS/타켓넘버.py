# n개의 음이 아닌 정수들이 있습니다
# 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 함

# 완전 탐색만 생각남...
from collections import deque 

def solution(numbers, target):
    # 사용할 수 있는 숫자
    # 타겟
    
    n = len(numbers)
    q = deque()
    q.append((numbers[0], 0))
    q.append((-numbers[0], 0))
    
    cnt = 0
    while q:
        val, index = q.popleft()  
        if index == n-1:
            if val == target:
                cnt += 1
            continue
            
        
        q.append((val + numbers[index+1], index+1))
        q.append((val - numbers[index+1], index+1))
        
    return cnt
    # 타겟 넘버를 만드는 방법의 수
    
    