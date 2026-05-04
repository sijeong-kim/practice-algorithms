n = int(input())
flower = []

for i in range(n):
    sm, sd, em, ed = map(int, input().split())
    flower.append((sm*100 + sd, em*100 + ed)) # MMdd

result = 0

day = 301
temp = day
idx = 0

flower.sort()

endtime = 301

# print(flower)
while endtime <= 1130:
    
    flag = False
    t = endtime

    # print("idx: ", idx, "t: ", t, "endtime: ", endtime)

    while idx < n:
        if flower[idx][0] > endtime:
            break
        if flower[idx][1] > t:
            t = flower[idx][1]
            idx += 1
            flag = True
        else:
            idx += 1

    endtime = t
    
    if flag:
        result += 1
    else:
        result = 0
        break

print(result)