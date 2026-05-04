import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

# root left right
def preOrder(inS, inE, postS, postE):
    if inS > inE or postS > postE:
        return

    # root
    root = postOrder[postE]
    print(root, end=" ")

    # left 
    preOrder(inS, idx[root]-1, postS, postS+idx[root]-1-inS)
    # right
    preOrder(idx[root]+1, inE, postE-inE+idx[root], postE-1)



n = int(input())
inOrder = list(map(int, input().split())) 
postOrder = list(map(int, input().split()))
# left root right
# left right root

idx = [0]*(n+1)
for i in range(n):
    idx[inOrder[i]] = i

preOrder(0, n-1, 0, n-1)
