# 탐색 시작점을 모르기 때문에 전체를 돌면서 1인 지점에서 탐색을 시작한다.
# 탐색 중 1인 부분은 0으로 바꿔 다시 방문하지 않도록 하고
# 한번의 BFS가 끝나게 되면 더 이상 확장이 불가능 하므로 마을 하나가 탄생하게 된다.
# 정사각형


from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
  n = len(graph)
  dq = deque()
  dq.append((a,b))
  graph[a][b]=0
  count = 1

  while dq:
    x,y = dq.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >=n:
        continue
      if graph[nx][ny] ==1:
        graph[nx][ny] = 0
        dq.append((nx,ny))
        count += 1
  return count

n = int(input())
graph =[]
for i in range(n):
  graph.append(list(map(int,input())))

cnt = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
  print((cnt[i]))


  #### DFS