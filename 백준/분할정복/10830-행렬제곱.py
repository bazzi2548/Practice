n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def mul(array, array2):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for l in range(n):
            for j in range(n):
                result[i][l] += array[i][j] * array2[j][l]
            result[i][l] %= 1000

    return result

def divide(arr, b):
    if b == 1:
        return arr
    if b == 2:
        return mul(arr, arr)
    else:
        temp = divide(arr, b//2)
        if b % 2 == 0:
            return mul(arr)
        else:
            return mul(mul(temp, temp), arr)

result = divide(arr, b)

for i in range(n):
    for j in range(n):
        print(result[i][j] % 1000, end=' ')
    print()