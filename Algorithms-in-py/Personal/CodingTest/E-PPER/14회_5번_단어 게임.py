# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 실제 시험에서는 Solution 클래스의 solution 함수를 사용합니다. 이를 감안하여 풀이해주세요.
INF = int(1e5) + 1
k, n = map(int, input().split())

words = []
for _ in range(k):
    words.append([input(), 0])
words.sort()

for _ in range(n):
    char = input()
    idx = 0
    count = INF
    for i in range(len(words)):
        if words[i][0][0] == char:
            if count > words[i][1]:
                count = words[i][1]
                idx = i  # 답 인덱스
    words[idx][1] += 1
    print(words[idx][0])