n = int(input())
count = n # 좋은 단어 개수
for _ in range(n):
    stack = []
    str = input()
    for char in str:
        if len(stack) != 0:
            if stack[-1] == char:
                stack.pop()
                continue
        stack.append(char)
    if len(stack) != 0:
        count -= 1

print(count)