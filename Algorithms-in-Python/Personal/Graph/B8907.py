import sys
input = sys.stdin.readline
from itertools import combinations

def isTriangle(case):

    c = 0
    # red
    isRedTriangle = True
    for edge in combinations(case, 2):
        if reds[edge[0]][edge[1]] == 0:
            isRedTriangle = False
            break
    if isRedTriangle:
        c += 1
    

    # blue
    isBlueTriangle = True
    for edge in combinations(case, 2):
        if blues[edge[0]][edge[1]] == 0:
            isBlueTriangle = False
            break
    if isBlueTriangle:
        c += 1
    
    return c
    


t = int(input())

for _ in range(t):
    v = int(input())

    reds = [[0]*(v+1) for _ in range(v+1)]
    blues = [[0]*(v+1) for _ in range(v+1)]

    for i in range(1, v):
        l = list(map(int, input().split()))
        for j in range(v-i):
            if l[j] == 1:
                reds[i][i+j+1] = 1
                reds[i+j+1][i] = 1
            else:
                blues[i][i+j+1] = 1
                blues[i+j+1][i] = 1

    count = 0
    cases = [(i+1) for i in range(v)]
    for case in combinations(cases, 3):
        count += isTriangle(case)
    
    print(count)
