import time
start = time.time()
import sys
input = sys.stdin.readline

n = int(input())
graph = []

attacked = []
for i in range(n):
    graph.append(list(input()))

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'O':
            for k in range(4):
                ni = i
                nj = j
                while True:
                    ni += move[k][0]
                    nj += move[k][1]
                    if 0<=ni<n and 0<=nj<n:
                        if graph[ni][nj] == ".":
                            graph[ni][nj] = "Y"
                        else:
                            break
                    else:
                        break
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'X':
            for k in range(4):
                ni = i
                nj = j
                while True:
                    ni += move[k][0]
                    nj += move[k][1]
                    if 0<=ni<n and 0<=nj<n:
                        if graph[i][j] != 'C' and graph[ni][nj] == ".":
                            graph[ni][nj] = "B"
                            graph[i][j] = 'C'
                            break
                        else:
                            break
                    else:
                        break

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'Y':
            print(".", end="")
        elif graph[i][j] == 'C':
            print("X", end="")
        else:
            print(graph[i][j], end="")
    print()

end = time.time()
print(f"{end-start:.5f} sec")