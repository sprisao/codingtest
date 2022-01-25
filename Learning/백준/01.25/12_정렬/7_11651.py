import sys
input = sys.stdin.readline

N = int(input())
pq = []

for _ in range(N):
    a, b = map(int, input().split())
    rev = [b, a]
    pq.append(rev)
b = sorted(pq)
for i in range(N):
    print(b[i][1], b[i][0])
