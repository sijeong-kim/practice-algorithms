import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())

shapes = list(map(int, input().split()))
count = [0] * 4
for shape in shapes:
    count[shape] += 1

# shapes = [1, 3, 3, 2, 1, 1, 3, 2]
# count = [0, 3, 2, 3]

mVal = int(1e9)

for order in permutations([1, 2, 3]):
    # order = [3 2 1]
    # aim = [3, 3, 3, 2, 2, 1, 1, 1]
    # pos[i][j] = i 구역에 있는 j 개수

    aim = []
    for i in order:
        aim += [i]*count[i]
    
    pos = [[0]*(4) for _ in range(4)]

    for i in range(n):
        pos[aim[i]][shapes[i]] += 1

    mVal = min(mVal, pos[1][2]+pos[1][3]+max(pos[2][3], pos[3][2]))

    
print(mVal)