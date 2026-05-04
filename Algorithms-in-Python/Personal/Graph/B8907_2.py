
t = int(input())

for _ in range(t):
    v = int(input())
    cnt = [0] * (v+1)

    for i in range(1, v):
        l = list(map(int, input().split()))
        for j in range(v-i):
            if l[j] == 1:
                cnt[i] += 1
                cnt[i+j+1] += 1
    s = 0
    for i in range(1, v+1):
        s += cnt[i] * (v-1-cnt[i])

    result = v*(v-1)*(v-2)//6 - s//2

    print(result)