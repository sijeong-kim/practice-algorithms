def find_parent(a):
    if parent[a]!=a:
        parent[a]=find_parent(a)
    return parent[a]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b]=a
    else:
        parent[a]=b
    
n, m=map(int, input().split())
parent=[0]*(n+1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(n+1):
    parent[i] = i

# 각 연산을 하나씩 확인
for _ in range(m):
    op, a, b=map(int, input().split())
    # 합집합(union) 연산인 경우
    if op==0:
        union_parent(a, b)
        break
    # 찾기(find) 연산인 경우
    elif op==1:
        if find_parent(a)==find_parent(b):
            print("YES")
        else:
            print("NO")

    
