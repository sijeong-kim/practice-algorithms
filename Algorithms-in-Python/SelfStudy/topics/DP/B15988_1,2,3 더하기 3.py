array=[0]*1000001
array[1]=1
array[2]=2
array[3]=4
for i in range(4, 1000001):
    array[i]=(array[i-3]+array[i-2]+array[i-1])%1000000009
for _ in range(int(input())):
    n=int(input())
    print(array[n])

         
