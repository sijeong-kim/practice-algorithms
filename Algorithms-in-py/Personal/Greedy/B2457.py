day_30 = [4, 6, 9, 11]
day_31 = [1, 3, 5, 7, 8, 10, 12]

def cal_day(month, day):
    result = day
    for m in range(1, month):
        if m in day_30:
            result += 30
        elif m in day_31:
            result += 31
        else:
            result += 28
    return result

n = int(input())
flower = []
left = cal_day(3, 1)
right = cal_day(11, 30)

for i in range(n):
    sm, sd, em, ed = map(int, input().split())
    startD = cal_day(sm, sd)
    if startD < left:
        startD = left
    endD = cal_day(em, ed)-1
    if endD > right:
        endD = right
    if startD <= endD:
        flower.append([startD, endD])

# flower.sort(key=lambda x : (x[0], -x[1]))
# print("flower: ", flower)

result = 0
while left <= right:
    # print("left: ", left, "right: ", right)

    # 정렬
    flower.sort(key=lambda x: (x[0], -x[1]))
    # print("flower: ", flower)

    # start, end
    start = flower[0][0]
    end = flower[0][1]

    if start != left:
        result = 0
        break

    result += 1
    
    # 제거하기
    # flower.pop(0)
    # for i in range(len(flower)):
    #     if flower[i][1] <= end:
    #         flower.pop(i)
    #         continue
    #     if flower[i][0] < start:
    #         flower[i][0] = start
    #         if flower[i][0] > flower[i][1]:
    #             flower.pop(i)

    new = []
    for item in flower:
        if item[1] <= end:
            continue
        if item[0] <= end:
            item[0] = end+1
            if item[0] > item[1]:
                continue
        new.append(item)
    flower = new
    left = end + 1

print(result)