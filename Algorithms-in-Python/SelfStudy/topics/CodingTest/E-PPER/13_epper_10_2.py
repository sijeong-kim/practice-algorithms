ans = 1

def solution(n, str):
    global ans

    print(str)
    if n == 0:
        return

	# print(str)
    for i in range(n):
        arr = []
        if len(str[i]) == 1:
            ans += 1
            
            count = 0
            for j in range(n):
                if i == j:
                    continue
                if str[i][0] in str[j]:
                    str[j].remove(str[i][0])
                    arr.append(str[j])
                    str[j] = []
                    count += 1

            solution(count, arr)


n = int(input())
str = []
for i in range(n):
	str.append(input())

for i in range(len(str)):
    str[i] = sorted(str[i]) # 문자열 정렬
    # print(str[i])

str.sort()

tem = []
for i in range(len(str)):
    isOk = True # 

    # 중복 제거
    if str[i] in tem:
        continue

    # 포함되어 있는 문자열인지 확인

    for j in range(len(str)):
        if i == j:
            continue

        # 한 문자라도 포함되어 있지 않다면 다른 문자
        isContained = True
        for k in range(len(str[i])):
            if str[i][k] not in str[j]:
                isContained = False
                break
        if isContained:
            isOk = False
            break
    
    if isOk:
        tem.append(str[i])

solution(len(tem), tem)

print(ans)