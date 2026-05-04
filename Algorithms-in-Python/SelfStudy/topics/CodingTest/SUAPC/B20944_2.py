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
    s += chr(i%26+97)

print(s, end="")

if pr:
    print(chr(pq%26+97), end="")

print(s[::-1], end="")

if r:
    print(chr(p%26+97), end="")

print(s, end="")

if pr:
    print(chr(pq%26+97), end="")
print(s[::-1], end="")

print()

end = time.time()

print(f"{end-start:.5f} sec")