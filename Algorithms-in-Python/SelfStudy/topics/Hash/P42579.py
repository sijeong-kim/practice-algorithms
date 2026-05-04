def solution1(genres, plays):
    hashmap = {}
    n = len(genres)
    
    for i in range(n):
        if genres[i] not in hashmap:
            hashmap[genres[i]] = [plays[i]]
        else:
            hashmap[genres[i]][0] += plays[i]
        hashmap[genres[i]].append((plays[i], i))

    # 장르 기준 내림차순 정렬
    values = list(hashmap.values())
    values.sort(key=lambda x : -x[0])

    print(values)
    ans = []
    for val in values:
        val = val[1:]
        
        # 장르 내 재생횟수 기준 내림차순 정렬
        # 장르 내 재생횟수 같은 경우 고유 번호가 낮은 노래 먼저 수록
        val.sort(key=lambda x: (-x[0], x[1]))
        # 수록
        ans.append(val[0][1])
        if len(val) > 1:
            ans.append(val[1][1])
    return ans

def solution2(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer



genres=["classic", "pop", "classic", "classic", "pop", "zazz", "zazz"]
plays = [500, 600, 150, 800, 2500, 2100, 1000]
print(solution2(genres, plays))

# 정답: [4, 1, 5, 6, 3, 0]

