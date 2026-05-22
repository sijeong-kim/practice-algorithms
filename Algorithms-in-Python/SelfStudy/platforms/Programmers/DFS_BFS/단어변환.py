

def solution(begin, target, words):

    if target not in words:
        return 0
    from collections import deque

    used = [False] * len(words)

    def one_diff(word1, word2):
        return sum([a != b for a, b in zip(word1, word2)]) == 1

    q = deque()
    q.append((begin, 0)) # 현재 단어, 변환 횟

    while q:
        curr, num = q.popleft()
        if curr == target:
            return num

        for i, word in enumerate(words):
            if used[i]: continue
            if one_diff(curr, word):
                q.append((word, num+1))
                used[i] = True


if __name__ == "__main__":
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]

    answer = solution(begin, target, words)
    print(answer)