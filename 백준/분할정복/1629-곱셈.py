import sys
a, b, c = map(int, sys.stdin.readline().split())

def solve(A, B):
    if B == 1:
        return A % c
    else:
        num = solve(A, B//2)
        if B%2 == 0:
            #곱셈이 짝수 번 이루어질 때
            return num*num%c
        else:
            #곱셈이 홀수 번 이루어질 때
            return num*num*A%c

print(solve(a, b))