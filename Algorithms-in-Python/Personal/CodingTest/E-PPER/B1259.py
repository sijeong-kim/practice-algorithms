import sys
input = sys.stdin.readline

while True:
    num = input().strip()
    if num == "0":
        break
    isP = True
    for i in range(len(num)//2):
        # print("i: ", i)
        # print("num[i], num[-1-i]: ", num[i], num[-1-i])
        if num[i] != num[-1-i]:
            print("no")
            isP = False
            break
    if isP:
        print("yes")