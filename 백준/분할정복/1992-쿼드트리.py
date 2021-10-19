import sys
input = sys.stdin.readline

N = int(input())
arr = [list(input()) for _ in range(N)]
result = ""

def quad_tree(x, y, n):
    global result
    num = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if num != arr[i][j]:
                result += "("
                quad_tree(x, y, n//2)
                quad_tree(x, y+n//2, n//2)
                quad_tree(x+n//2, y, n//2)
                quad_tree(x+n//2, y+n//2, n//2)
                result += ")"
                return
    if num == "1":
        result += "1"
    else:
        result += "0"
quad_tree(0, 0, N)
print(result)
