def solution(progresses, speeds):
    # 각 기능은 진도 100%일 때 서비스 반영 가능
    # 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고
    # 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됨
    
    # 배포 되어야하는 순서대로 작업 진도가 적힌 정수 배열 parogresses
    # 각 작업의 개발 속도가 적힌 정수 배열 speeds
    
    # queue task 단위로, 하나씩 넣고 queue[0] 보다 작은 것들 개수 세기
    import math
    from collections import deque
    
    def find_remains(p, s):
        return math.ceil((100 - p)/s)
    
    remains = [find_remains(p,s) for p, s in zip(progresses, speeds)]
    
    print(remains)
    answer = []
    q = deque()
    
    for r in remains:
        if not q or (q and q[0] >= r):
            q.append(r)
        else:
            cnt = 0
            while q:
                q.popleft()
                cnt += 1
            answer.append(cnt)
            q.append(r)
            
    cnt = 0
    while q:
        q.popleft()
        cnt += 1
    answer.append(cnt)

    # 배포마다 몇 개의 기능이 배포되는지
    return answer