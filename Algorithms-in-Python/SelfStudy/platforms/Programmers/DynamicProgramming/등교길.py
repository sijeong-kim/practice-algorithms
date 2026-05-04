def solution(m, n, puddles):
    
    DIV = 1000000007
    # puddles
    # 오른쪽, 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단 경로의 개수
    # m, n: 1 이상 100이하
    # 물에 잠긴 경우
    
    map = [[0]*m for _ in range(n)]
    
    for x, y in puddles:
        map[y-1][x-1] = -1
    
    for i in range(n):
        if map[i][0] == -1:
            break
        map[i][0] = 1
        
    for j in range(m):
        if map[0][j] == -1:
            break
        map[0][j] = 1
        
    for i in range(1, n):
        for j in range(1, m):
            
            # 웅덩이 경우 0
            if map[i][j] == -1: continue
            
            
            left = 0 if map[i][j-1] == -1 else map[i][j-1]
            up = 0 if map[i-1][j] == -1 else map[i-1][j]
            
            map[i][j] = (left + up) % DIV
                
    return 0 if map[n-1][m-1] == -1 else map[n-1][m-1]