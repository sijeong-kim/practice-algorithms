star = [[0] * 13 for _ in range(13)]
count = [0] * 13

for i in range(12):
    x, y = map(int, input().split())
    star[x][y] = 1
    star[y][x] = 1
    count[x] += 1
    count[y] += 1

adj = [1, 2, 3]
ans = -1

# 차수가 3인 별에 대해 조사
# 각 별의 차수를 리스트에 담아 Spica와 같은지 확인

for i in range(1, 13):
    
    tAdj=[]
    if count[i] == 3:
        for j in range(1, 13):
            if star[i][j]==1:
                tAdj.append(count[j])

        if sorted(tAdj) == adj:
            ans = i
            break
            
print(ans)
