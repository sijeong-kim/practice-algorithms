import sys
input = sys.stdin.readline


def solution(r, c, zr, zc, article):
    for i in range(r):
        for zi in range(zr):
            for j in range(c):
                for zj in range(zc):
                    if article[i][j] == '\n':
                        continue
                    print(article[i][j], end = '')
            print()

r, c, zr, zc = map(int, input().split())

article = []
for i in range(r):
    article.append(list(input()))

solution(r, c, zr, zc, article)