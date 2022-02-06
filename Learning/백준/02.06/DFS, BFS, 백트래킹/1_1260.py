from collections import deque

N, M, V = map(int, input().split())

adj = [[0] * (N +1) for _ in range(N +1)]


for _ in range(M):
  m1, m2 = map(int, input().split())
  adj[m1][m2] = adj[m2][m1] =1



# for row in adj:
#   print(row)

def bfs(start_v): ## 시작점
  discovered = [start_v]
  dq = deque()
  dq.append(start_v)

  while dq:
    v = dq.popleft()
    print(v, end=' ')

    for w in range(len(adj[start_v])):
      if adj[v][w] == 1 and (w not in discovered):
        discovered.append(w)
        dq.append(w)

def dfs(start_v, discovered = []):  ## BFS와는 다르게 discovered를 인자로 같이 정의해준다. 
  discovered.append(start_v)
  print(start_v, end=' ')
  for w in range(len(adj[start_v])):
    if adj[start_v][w] == 1 and (w not in discovered):
      dfs(w, discovered)

dfs(V)
print()
bfs(V)
