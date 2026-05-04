n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i]<b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

#처음 정렬하지 않고 min(), max()를 사용하여 짠 코드
#count=0
#while min(a)<max(b) and count<k :
#    a[a.index(min(a))], b[b.index(max(b))] = b[b.index(max(b))], a[a.index(min(a))]
#    count+=1

print(sum(a))

