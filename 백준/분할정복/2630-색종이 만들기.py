import sys
input = sys.stdin.readline

def quad_tree(x, y, n):
    num = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != paper[i][j]:
                quad_tree(x, y, n//2)
                quad_tree(x, y+n//2, n//2)
                quad_tree(x+n//2, y, n//2)
                quad_tree(x+n//2, y+n//2, n//2)
                return
    if num == 0:
        result.append(0)
    else:
        result.append(1)

N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
result = []

quad_tree(0,0,N)
print(result.count(0))
print(result.count(1))
