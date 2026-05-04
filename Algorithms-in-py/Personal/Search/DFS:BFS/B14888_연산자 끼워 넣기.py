n=int(input())
data = list(map(int, input()))
op = list(map(int, input()))

# 최솟값과 최댓값 초기화

min_value=1e9
max_value=-1e9

# 깊이 우선 탐색 (DFS) 메서드
def dfs(i, now):
    global min_value, max_value, op
    
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i==n:
        min_value=min(min_value, now)
        max_value=max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if op[0]>0:
            op[0]-=1
            dfs(i+1, now+data[i])
            op[0]+=1
        if op[1]>0:
            op[1]-=1
            dfs(i+1, now-data[i])
            op[1]+=1
        if op[2]>0:
            op[2]-=1
            dfs(i+1, now*data[i])
            op[2]+=1
        if op[3]>0:
            op[3]-=1
            dfs(i+1, int(now/data[i])) # 나눌 때 나머지 제거
            op[3]+=1

#DFS 메서드 호출
dfs(1, data[0])

#최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)

    
