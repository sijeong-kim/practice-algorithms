import math
import sys
input = sys.stdin.readline

length, width, height = map(int, input().split())

n = int(input())
cubes = []
for i in range(n):
    cubes.append(list(map(int, input().split())))

# 큐브 종류 올림차순 정렬
cubes.sort()

count = 0
flag = True
def backtracking(i, length, width, height):
    global count
    global flag
    # print("==================")
    # print(i, length, width, height)

    if flag == False:
        return
    if length==0 or width==0 or height==0:
        return
    if i == -1:
        flag = False
        return

    cube_side = int(math.pow(2, cubes[i][0]))

    lq = length // cube_side
    wq = width // cube_side
    hq = height // cube_side
    lr = length % cube_side
    wr = width % cube_side
    hr = height % cube_side

    # 큐브 사용 못함 -> 더작은 큐브로
    if lq == 0 or wq == 0 or hq == 0:
        backtracking(i-1, length, width, height)
    
    # 필요한 개수 충족
    need_num = lq*wq*hq
    if need_num <= cubes[i][1]:
        # print("충분: ", need_num, cubes[i][1])
        cubes[i][1] -= need_num
        count += need_num

    # 부족 시 더 작은 큐브로
    else:
        # print("부족: ", need_num, cubes[i][1])
        need_num -= cubes[i][1]
        count += cubes[i][1]
        cubes[i][1] = 0

        for j in range(need_num):
            backtracking(i-1, cube_side, cube_side, cube_side)
    
    # 나머지 찾기
    print(i, "나머지 찾기 시작")
    backtracking(i-1, lr, width-wr, height-hr)
    backtracking(i-1, length-lr, wr, height-hr)
    backtracking(i-1, length-lr, width-wr, hr)
    backtracking(i-1, length-lr, wr, hr)
    backtracking(i-1, lr, width-wr, hr)
    backtracking(i-1, lr, wr, height-hr)
    backtracking(i-1, lr, wr, hr)
    print("나머지 찾기 끝")

backtracking(n-1, length, width, height)

if flag:
    print(count)
else:
    print("-1")