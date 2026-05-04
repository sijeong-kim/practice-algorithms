str = input()

l = len(str)

num1 = str[:l//2]
num2 = str[l//2:]

sum1 = 0
sum2 = 0

for i in num1:
    sum1 += int(i)

for i in num2:
    sum2 += int(i)

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")
