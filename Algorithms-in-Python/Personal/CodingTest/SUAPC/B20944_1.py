import time
start = time.time()

import sys
input = sys.stdin.readline

n = int(input())
p = n//2
r = n%2

pr = p%2
pq = p//2

s = ""

for i in range(pq):
    # print(chr(i%26+97), end="")
    s+=(chr(i%26+97))

if pr:
    # print(chr(pq%26+97), end="")
    s+=(chr(pq%26+97))

for i in range(pq-1, -1, -1):
    # print(chr(i%26+97), end="")
    s+=(chr(i%26+97))

print(s, end="")

if r:
    print(chr(p%26+97), end="")

# print(s[::-1])
print(s)

# for i in range(pq):
#     print(chr(i%26+97), end="")
#     # s+=(chr(i%26+97))

# if pr:
#     print(chr(pq%26+97), end="")
#     # s+=(chr(pq%26+97))

# for i in range(pq-1, -1, -1):
#     print(chr(i%26+97), end="")
#     # s+=(chr(i%26+97))


end = time.time()

print(f"{end-start:.5f} sec")