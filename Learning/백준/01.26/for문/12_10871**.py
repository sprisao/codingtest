import sys
input = sys.stdin.readline

N, X = map(int, input().split())


# '1 10 4 9 2 3 8 5 7 6' 이런식으로 숫자를 일렬로 받아올때 -> 리스트로 정의해서 int를 기준으로 나누어 담는당
A = list(map(int, input().split()))

result = []
for i in A:
    if i < X:
        result.append(i)

print(*result)
