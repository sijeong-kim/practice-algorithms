n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))

a.sort()
b.sort()

def binary_sort(array, target, start, end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

start=0
for item in b:
    result=binary_sort(a, item, start, len(a))
    if result==None:
        print('no', end=' ')
    else:
        start=result
        print('yes', end=' ')
