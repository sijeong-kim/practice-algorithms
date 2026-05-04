import sys
input = sys.stdin.readline

t = int(input())

ans = []
while (t > 0):
    t -= 1
    n = int(input())
    a = list(input().rstrip())
    b = list(input().rstrip())

    dif_zero = 0
    dif_one = 0
    same_zero = 0
    same_one = 0

    for i in range(n):
        if a[i] != b[i]:
            if a[i] == '0':
                dif_zero += 1
            else:
                dif_one += 1
        else:
            if a[i] == '0':
                same_zero += 1
            else:
                same_one += 1

    ans1 = ans2 = ans3 = ans4 = int(1e9)

    if same_one + same_zero == n:
        ans4 = 0

    if dif_one % 2 == 0 and dif_one - dif_zero == 0:
        ans1 = dif_one + dif_zero
    else:
        if same_one % 2 == 0 and same_one - same_zero == 1:
            ans2 = same_one + same_zero
        else:
            ans2 = -1

    ans.append(min(ans1, ans2, ans3, ans4))

for i in ans:
    print(i)