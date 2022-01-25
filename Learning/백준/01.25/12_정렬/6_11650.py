# 힙 문제일것 같다. -> (X)
# 틀렸다, map으로 푸는 문제다.
# 입력 받는 방식:
# 5
# 3 4
# 1 1
# 1 - 1
# 2 2
# 3 3
# 이럴땐 map과 split을 사용해야 한다.

import heapq as hq
import sys

input = sys.stdin.readline

N = int(input())
pq = []

for _ in range(N):
    a, b = map(int, input().split())
    pq.append((a, b))
    # '튜플' 형식으로 이렇게 append하는데 특히 append()안에 (a, b)를 다시한번 넣어주는 것을 살펴라
pq.sort()

for i in range(N):
    print(pq[i][0], pq[i][1])
