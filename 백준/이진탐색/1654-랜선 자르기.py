import sys
input = sys.stdin.readline

k, n = map(int, input().split()) # n은 타겟값
array = []

for i in range(k):
    array.append(int(input()))

start = 1
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in array:
        total += i // mid

    if total < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)

