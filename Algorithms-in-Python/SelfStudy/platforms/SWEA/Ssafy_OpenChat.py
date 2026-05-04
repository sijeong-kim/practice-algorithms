nums = [1, 1, 2, 5, 6, 14, 31, 33]

#### DP ####

n = sum(nums)

dp = [False] * (n+1)
dp[0] = True

for num in nums: # 순서대로 숫자를 사용해서 만들 수 있는지 확인
    for s in range(n, num-1, -1): # 합
        if dp[s-num]: # s-num 을 만들 수 있으면 s 를 만들 수 있음
            dp[s] = True

for i in range(n):
    if not dp[i]:
        answer = i
        break

print(bin(answer)[2:])


#### Greedy ####
nums.sort()

reachable = 0

for num in nums:
    # 기존 만들 수 있는 수: 0, 1, 2, ..., reachable
    # reachable < num - 1 이면 더 이상 만들 수 없음
    if reachable < num - 1:
        break
    reachable += num
    # 새로 만들 수 있는 수: num, num + 1, num + 2, ... num + reachable
    
answer = reachable + 1
print(bin(answer)[2:])