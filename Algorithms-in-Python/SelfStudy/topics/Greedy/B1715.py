import sys, heapq
input = sys.stdin.readline
n = int(input())
cards = []
for i in range(n):
    card = int(input())
    heapq.heappush(cards, card)

ans = 0
while len(cards) != 1:
    s1 = heapq.heappop(cards)
    s2 = heapq.heappop(cards)
    ans += s1+s2
    heapq.heappush(cards, s1+s2)

print(ans)