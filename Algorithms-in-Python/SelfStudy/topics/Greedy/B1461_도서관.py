n, m = map(int, input().split())
books = list(map(int, input().split()))
books.sort()

pos = []
neg = []

max_val = 0
for book in books:
    max_val = max(abs(book), max_val)
    if book > 0:
        pos.append(book)
    else:
        neg.append(abs(book))

neg.sort()

ans = 0

# pos_q = len(pos) // m
# if pos_q != 0:
for i in range(len(pos)-1, -1, -m):
    ans += pos[i] * 2
# else:
#     ans += pos[-1]

# neg_q = len(neg) // m
# if neg_q != 0:
for i in range(len(neg)-1, -1, -m):
    ans += neg[i] * 2
# else:
#     ans += neg[-1]

print(ans - max_val)