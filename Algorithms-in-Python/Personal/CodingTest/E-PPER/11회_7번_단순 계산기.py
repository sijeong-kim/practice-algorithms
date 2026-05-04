# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(num_arr, n):
    sol = 0
    num_arr.sort()
    # print(num_arr)

    # 	t = 1
    # 	for i in range(n-1, 0, -1):
    # 		t *= 2
    # 		x = num_arr[i] / t
    # 		sol += x
    # 		print('%.6f' %sol)

    # 	sol += num_arr[0] / t

    idx1 = 0
    idx2 = 1
    for i in range(n - 1):
        num_arr[idx2] = (float)(num_arr[idx1] + num_arr[idx2]) / 2
        # print('%.6f' %num_arr[idx2])
        idx1 += 1
        idx2 += 1

    sol = num_arr[n - 1]

    return sol


n = int(raw_input())
num_arr = []
for i in range(n):
    num_arr.append(int(raw_input()))
print('%.6f' % solution(num_arr, n))