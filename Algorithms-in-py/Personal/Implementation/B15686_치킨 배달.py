import itertools

# 입력
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 치킨 집 위치
stores = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            stores.append((i, j))

result = 10000
for case in itertools.combinations(stores, m):
    total = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                tem = 101
                for store in case:
                    tem = min((abs(store[0]-i) + abs(store[1]-j)), tem)
                total += tem
    result = min(result, total)

print(result)
