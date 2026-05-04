import sys
input = sys.stdin.readline

idx = [0, 0, 0, 0] # 정각 인덱스

def rotation(num, dir):
    
    rotDir = [0, 0, 0, 0] # 회전 방향 임시 리스트
    rotDir[num] = dir

    # 오른쪽으로 톱니바퀴 체크
    for i in range(num, 3):
        # print("오른쪽 - num, i: ", num, i)
        if rotDir[i] == 0:
            break
        if wheels[i][(idx[i]+2)%8] == wheels[i+1][(idx[i+1]+6)%8]:
            break
        rotDir[i+1] = (-1) * rotDir[i]

    # 왼쪽으로 톱니바퀴 체크
    for i in range(num, 0, -1):
        # print("왼쪽 - num, i: ", num, i)
        if rotDir[i] == 0:
            break
        if wheels[i][(idx[i]+6)%8] == wheels[i-1][(idx[i-1]+2)%8]:
            break
        rotDir[i-1] = (-1) * rotDir[i]

    # 인덱스 회전
    for i in range(4):
        rd = rotDir[i]
        if rd != 0:
            idx[i] = (idx[i] - rd) % 8

# 입력
wheels = []
for i in range(4):
    wheels.append(input())

k = int(input())
for i in range(k):
    num, dir = map(int, input().split())
    num -= 1
    # 회전
    rotation(num, dir)

result = 0
for i in range(4):
    if wheels[i][idx[i]] == '1':
        result += 1 << i

print(result)

