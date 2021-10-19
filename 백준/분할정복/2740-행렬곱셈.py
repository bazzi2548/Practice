import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(m)]

result = [[0 for i in range(k)] for _ in range(n)]

for x in range(n):
    for y in range(k):
        for z in range(m):
            result[x][y] += A[x][z] * B[z][y]

for x in range(n):
    for y in range(k):
        print(result[x][y], end=" ")
    print()