import sys
input = sys.stdin.readline

minV = int(1e9)

visited = [0] * 50


def checkNeighbor(begin, word):
    cnt = 0
    m = len(begin)
    for i in range(m):
        if begin[i] != word[i]:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False

def dfs(begin, target, words, cnt):
    global minV

    if begin == target:
        if cnt < minV:
            minV = cnt
        return

    for i in range(len(words)):
        if checkNeighbor(begin, words[i]):
            if visited[i] == 0:
                visited[i] = 1
                dfs(words[i], target, words, cnt+1)
                visited[i] = 0
            else:
                continue


def solution(begin, target, words):

    n = len(words)
    table = [[] for i in range(n+1)]


    for word in words:
        if checkNeighbor(begin, word):
            table[0].append(word)
    for i in range(n):
        for j in range(n):
            if checkNeighbor(words[i], words[j]):
                table[i+1].append(words[j])
        
    dfs(begin, target, words, 0)

    if minV < int(1e9):
        return minV
    else:
        return 0

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))