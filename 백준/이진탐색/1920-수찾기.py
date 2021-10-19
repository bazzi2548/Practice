import sys
input = sys.stdin.readline

# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
array2 = list(map(int, input().split()))

for i in array2:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print("1")
    else:
        print(0)