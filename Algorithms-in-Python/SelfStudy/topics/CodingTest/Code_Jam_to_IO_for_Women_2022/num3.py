import sys
input = sys.stdin.readline

def backtracking(now, total):
    global ans
    if len(not_visited) == 0:
        if ans > total: 
            ans = total
        return
    for next, cost in graph[now]:        
        if visit_cnt[next] == 0:
            continue
        visit_cnt[next] -= 1
        
        flag = False
        if next in not_visited:
            flag = True
            not_visited.discard(next)
        
        backtracking(next, total+cost)
        
        if flag:
            not_visited.add(next)
            
        visit_cnt[next] += 1
        

if __name__ == "__main__":
    INF = int(1e12) * 2
    t = int(input())
    cnt = 0
    while t > 0:
        t -= 1 
        cnt += 1
        
        n = int(input())
        graph = [[] for _ in range(n+1)]
        not_visited = {i for i in range(1, n+1)}
        visit_cnt = [0] * (n+1)
        
        ans = INF
        for i in range(n-1):
            a, b, c = map(int, input().split())
            graph[a].append((b, c))
            graph[b].append((a, c))
            visit_cnt[a] += 1
            visit_cnt[b] += 1
            
        
        for i in range(1, n+1):
            visit_cnt[i] -= 1
        
            flag = False
            if i in not_visited:
                flag = True
                not_visited.discard(i)
            
            backtracking(i, 0)
            
            if flag:
                not_visited.add(i)
                
            visit_cnt[i] += 1
        
        print(f"Case #{cnt}:", ans)
    
    
