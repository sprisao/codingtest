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
  chk = [start_v]
  dq = deque()
  dq.append(start_v)
  while dq:
    v = dq.popleft()
    print(v, end=' ')
    ###################
    for w in range(N+1):
      if adj[v][w] and (w not in chk):
        dq.append(w)
        chk.append(w)
    ###################
    
def dfs(start_v, chk=[]):
  chk.append(start_v)
  print(start_v, end=' ')
  ###################
  for w in range(N + 1):
    if adj[start_v][w] and (w not in chk):
      dfs(w, chk)
  ###################


dfs(V)
print()
bfs(V)