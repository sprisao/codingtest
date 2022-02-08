from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
  n = len(graph)
  dq = deque()
  dq.append((a,b))
  graph[a][b] = 0
  count = 1  #동 내 단지 수
  while dq:
    x, y = dq.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n :
        continue #벗어날경우 -> 패스
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        dq.append((nx,ny))
        count += 1 #단지 수 추가 
  return count

N = int(input())
graph = []
for i in range(N):
  graph.append(list(map(int, input())))


#이부분은 연결요소를 찾을 때 필요한 내용인가보다.
cnt = []
for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
  print((cnt[i]))