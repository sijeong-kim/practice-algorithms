def solution(n, costs):
    answer = 0
    parents = [i for i in range(n+1)]

    def find_parent(x):
        while parents[x] != x:
            x = parents[x]

        return parents[x]

    def union(a, b):
        parent_a = find_parent(a)
        parent_b = find_parent(b)
        if parent_a != parent_b:
            if parent_a < parent_b:
                parents[parent_b] = parent_a
            else:
                parents[parent_a] = parent_b
            return True
        else:
            return False

    cnt = n-1

    # 최소 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 최소 비용
    costs.sort(key=lambda x: x[2]) # cost 기준으로 오름차순 정렬
    for a, b, cost in costs:

        if union(a, b):
            answer += cost
            cnt -= 1

        if cnt == 0:
            break

    return answer


if __name__ == "__main__":
    n = 4
    costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

    answer = solution(n, costs)
    print(answer)
