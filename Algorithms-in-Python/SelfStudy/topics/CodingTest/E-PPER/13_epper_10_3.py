ans = 1

def solution(n, str):
    global ans

    print(str)
    if n == 0:
        return

	# print(str)
    for i in range(n):
        
        arr = []

        # 노드 하나 필요
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

for s in str:
    if s not in tem:
        tem.append(s)


solution(len(tem), tem)

print(ans)