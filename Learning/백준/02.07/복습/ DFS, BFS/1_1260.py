from dis import disco
import sys
from tracemalloc import start
input = sys.stdin.readline

from collections import deque

# 양방향
# DFS
# BFS

N, M, V = map(int,input().split())

adj = [[0]* (N +1 ) for _ in range(N+1)] # 정점의 개수가 1부터 시작하기 때문에

for _ in range(M):
  a, b = map(int, input().split())
  adj[a][b] = adj[b][a] = 1  #양방향이기 때문에

# for row in adj:
#   print(row)  # 정상적으로 출력된다.

def bfs(start_v):
  discovered = [start_v]
  dq = deque()
  # print(start_v, end=' ') ### <<- 여기서 출력하는게 아니네
  dq.append(start_v)
  while dq:
    v = dq.popleft() ### <<- 이부분 생각 안남
    print(v, end=' ')
    for w in range(N+1): ### <<- 이부분도 틀림
      # if adj[v][w] and (w not in discovered):
      if adj[v][w] == 1 and (w not in discovered):
        discovered.append(w)
        dq.append(w)
        # discovered = [w] <<-- 이부분도
        # bfs(w) <<-- 이거 필요 없다 
bfs(V)