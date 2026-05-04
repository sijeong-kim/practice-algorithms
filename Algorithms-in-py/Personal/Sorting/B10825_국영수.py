# BOJ 10825
n=int(input())
array=[]
for _ in range(n):
    array.append(input().split())

for student in sorted(array, key=lambda score: (-int(score[1]), int(score[2]), -int(score[3]), score[0])):
    print(student[0])
