str = input()

count = 0
pre = str[0]
for i in range(1, len(str)):
    if pre != str[i]:
        count += 1
        pre = str[i]

result = (count + 1) // 2
print(result)
