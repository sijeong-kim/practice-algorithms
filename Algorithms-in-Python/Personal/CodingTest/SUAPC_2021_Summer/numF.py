# import time
import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):

    # start = time.time()
    n, k = map(int, input().split())

    if n-k < 1:
        u = 1
    else:
        u = n-k

    sum = 2*((u+n)*(n-u+1))
    print(sum)

    # end = time.time()
    # print(f"{end-start:.5f} sec")


