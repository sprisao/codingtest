#양방향
#DFS

import sys
input = sys.stdin.readline

N = int(input()) #정점 
M = int(input()) #간선

adj = [[0] * (N + 1) for _ in range(N +1)]

for _ in range(M):
  a, b = map(int, input().split())
  adj[a][b] = adj[b][a] = 1

# for row in adj:
#   print(row)

def dfs(start_v, discovered=[]):
  discovered.append(start_v)
  dfs.cnt += 1
  for w in range(len(adj[start_v])):
    if adj[start_v][w] and (w not in discovered):
      dfs(w, discovered)
dfs.cnt = 0
dfs(1)
print(dfs.cnt -1 )