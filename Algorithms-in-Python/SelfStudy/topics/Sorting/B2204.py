import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    tem = 'Z'*20
    for i in range(n):
        word = input().rstrip()
        if word.upper() < tem.upper():
            tem = word
    print(tem)