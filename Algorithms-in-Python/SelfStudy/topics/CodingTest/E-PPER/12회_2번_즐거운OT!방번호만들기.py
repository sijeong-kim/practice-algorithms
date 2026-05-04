n = int(input())

room_n = (n-1) // 15 + 1
in_n = (n-1) % 15 + 1

print(str(room_n)+" "+str(in_n))