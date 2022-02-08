from collections import deque

M, N = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]

dq = deque([])

dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]
res = 0

for i in range(N):
  for j in range(M):
    if board[i][j] == 1:
      dq.append([i,j])

def bfs():
  while dq:
    x, y = dq.popleft()
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0 <= nx < N and 0<= ny < M and board[nx][ny]==0:
        board[nx][ny]= board[x][y] + 1
        dq.append([nx,ny])

bfs()

for n in board:
  for m in n:
    if m == 0 :
      print(-1)
      exit(0) 
  res = max(res, max(n)) 
print(res -1)