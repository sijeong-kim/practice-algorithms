import math
import sys
input = sys.stdin.readline

l, w, h = map(int, input().split())
length = int(math.pow(2, l))
width = int(math.pow(2, w))
height = int(math.pow(2, h))

n = int(input())
cubes = []
for i in range(n):
    cubes.append(list(map(int, input().split())))

# 큐브 종류 올림차순 정렬
cubes.sort()

flag = False

def backtracking(i, length, width, height):
    global flag
    if length==0 or width==0 or height==0:
        return 0
    if i == -1:
        flag = True
        print("안됨")
        return 0

    cube_side = int(math.pow(2, cubes[i][0]))

    lq = length // cube_side
    wq = width // cube_side
    hq = height // cube_side
    lr = length % cube_side
    wr = width % cube_side
    hr = height % cube_side

    # 큐브 사용 못함
    if lq == 0 or wq == 0 or hq == 0:
        print("큐브 사용 못함")
        return backtracking(i-1, length, width, height)
    
    # 필요한 개수 충족
    need_num = lq*wq*hq
    print("처음 need_num:", need_num)

    if need_num <= cubes[i][1]:
        cubes[i][1] -= need_num
        print("필요한 개수 충족", need_num)
        return need_num + backtracking(i-1, lr, wr, hr)

    # 부족 시 더 작은 큐브로
    need_num -= cubes[i][1]
    print("부족시 더 작은 큐브로", need_num)
    now = cubes[i][1]
    cubes[i][1] = 0
    smaller = backtracking(i-1, cube_side, cube_side, cube_side)
    remain = backtracking(i-1, lr, wr, hr)
    result = now + (need_num * smaller)+ remain
    print("now:", now)
    print("smaller:", smaller)
    print("remain:", remain)
    return result

ans = backtracking(n-1, length, width, height)

if flag:
    print("-1")
else:
    print(ans)

