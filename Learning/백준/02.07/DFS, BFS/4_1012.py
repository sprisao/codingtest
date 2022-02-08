#길찾기 문제
#연결요소
#1이 있는 값을 찾아라
#T = 테스트 케이스 개수
# M = 배추밭의 가로길이
# N = 배추밭의 세로길이
# K = 배투가 심어져 있는 위치의 개수
# X, Y = 배추의 위치

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1,0, 0]

  
def bfs(adj, a, b):
  chk = [(a,b)]
  dq = deque()
  dq.append((a,b))
  adj[a][b]=0
  while dq:
    x, y = dq.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      if adj[nx][ny] == 1:
        adj[nx][ny] = 0
        dq.append((nx,ny))


T = int(input())
for _ in range(T):
  cnt = 0
  N, M, K = map(int,input().split())
  adj= [[0]* (M) for _ in range(N)]
  for _ in range(K):
    x, y = map(int, input().split())
    adj[x][y] = 1
  for a in range(N):
    for b in range(M):
      if adj[a][b] == 1:
        bfs(adj, a, b)
        cnt += 1

  print(cnt)