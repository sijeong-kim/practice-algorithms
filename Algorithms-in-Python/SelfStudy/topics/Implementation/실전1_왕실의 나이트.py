x, y = input()
x = int(ord(x)) - int(ord('a')) + 1
y = int(y)

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

result = 0
for dx, dy in steps:
    nx = x + dx
    ny = y + dy
    if 1 > nx or nx > 8 or ny > 8 or 1 > ny:
        continue
    result += 1

print(result)
