
graph = [[] for _ in range(17)]
sheep = 0
wolf = 0
maxV = 0

def dfs(info, num):
    global maxV, sheep, wolf
    # if sheep <= wolf:
    #     return


    if info[num] == 0:
        info[num] = -1 # 수집함
        sheep += 1
    if info[num] == 1:
        wolf += 1

    print("num, sheep, wolf", num, sheep, wolf)

    if sheep <= wolf:
        wolf -= 1
        return
    if maxV < sheep:
        maxV = sheep

    children = graph[num]

    if len(children) == 2:
        children = [children[0], children[1], children[0]]
        for child in children:
            dfs(info, child)
        children = [children[1], children[0], children[1]]
        for child in children:
            dfs(info, child)
    else:
        for child in children:
            dfs(info, child)
            


def solution(info, edges):
    global sheep
    n = len(info)

    for edge in edges:
        graph[edge[0]].append(edge[1])

    print(graph)

    dfs(info, 0)
    
    return maxV

# info = [0,0,1,1,1,0,1,0,1,0,1,1]
# edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
print(solution(info, edges))
