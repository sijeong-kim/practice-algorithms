import heapq

def solution(N, road, K):
    answer = 0

    graph = [{} for _ in range(N + 1)]
    for a, b, c in road:
        if b not in graph[a]:
            graph[a][b] = c
            graph[b][a] = c
        elif graph[a][b] > c:
            graph[a][b] = c
            graph[b][a] = c

    INF = int(1e9)
    distance = [INF] * (N + 1)

    start = 1
    distance[start] = 0
    hq = [(0, 1)]
    heapq.heapify(hq)

    while hq:
        dist, curr = heapq.heappop(hq)

        # 벌써 갔던 곳이라면 무시
        if dist > distance[curr]:
            continue

        for next, cost in graph[curr].items():
            if distance[next] > distance[curr] + cost:
                heapq.heappush(hq, (distance[curr] + cost, next))
                distance[next] = distance[curr] + cost

    for i in range(1, N + 1):
        if distance[i] <= K:
            answer += 1

    return answer

if __name__ == "__main__":

    N = 5
    road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
    K = 3

    N = 6
    road= [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]]
    K = 4

    result = solution(N, road, K)
    print(result)
