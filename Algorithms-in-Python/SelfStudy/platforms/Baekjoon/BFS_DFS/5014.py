import sys
from collections import deque
input = sys.stdin.readline

# 총 F 층
# 스타트 링크 위치 G 층
# 강호가 있는 곳 S 층
# 엘리베이터를 타고 G층으로 이동
# 강호가 탄 엘리베이터 버튼 2개 - U 버튼, D 버튼 (층이 없을 땐 움직이지 않음)
# 강호가 G층에 도착하려면, 버튼을 적어도 몇 번 눌러야하는지 구하는 프로그램을 작성

# "use the stairs"

f, s, g, u, d = map(int, input().split())
button = 0

q = deque([(s-1, 0)])
visited = [False] * f
visited[s-1] = True

find=False
while q:
    curr, button = q.popleft()
    if curr == g-1:
        print(button)
        find = True
        break
    
    if 0 <= curr+u < f and not visited[curr+u]:
        q.append((curr+u, button+1))
        visited[curr+u] = True
        
    if 0 <= curr-d < f and not visited[curr-d]:
        q.append((curr-d, button+1))
        visited[curr-d] = True

if not find:
    
    print("use the stairs")