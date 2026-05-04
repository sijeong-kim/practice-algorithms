import math

def toMin(stringTime):
    c, m = map(int, stringTime.split(":"))
    return 60*c + m

def solution(fees, records):
    numbers = []
    infos = []
    for record in records:
        time, num, state = record.split(' ')
        if num not in numbers:
            numbers.append(num)
            infos.append([num, (toMin(time), state)])
        else:
            for i in range(len(infos)):
                if infos[i][0] == num:
                    infos[i].append((toMin(time), state))
    
    print(numbers)
    print(infos)

    infos.sort(key = lambda x: x[0])
    answer = []

    print(infos)
    for info in infos:
        total = 0
        if len(info) % 2 == 0:
            total = toMin("23:59") - info[-1][0]
            for j in range(len(info)-2, 1, -2):
                total += info[j][0] - info[j-1][0]
        else:
            for j in range(len(info)-1, 1, -2):
                total += info[j][0] - info[j-1][0]
        print(total)

        if total > fees[0]:
            ans = fees[1] + math.ceil((total-fees[0])/fees[2]) * fees[3]
        else:
            ans = fees[1]
        answer.append(ans)

    return answer




fees=[180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))