from collections import deque

N, M = map(int, input().split())
board = [input() for _ in range(N)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def is_valid_coord(y,x):
  return 0 <= y < N and 0 <= x < M

def bfs():
  chk = [[False] * M for _ in range(N)]
  chk[0][0] = True
  dq = deque()
  dq.append((0, 0, 1))  ## 0, 0 부터 시작하고 시작지점 포함이니까 1로 더해준다.
  while dq:
    y, x, d = dq.popleft()  

    if y == N - 1 and x == M - 1: ### 최종 종착점에 오면
      return d #d 값을 출력해준다.
 
    nd = d + 1 
    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]
      if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
        chk[ny][nx]= True
        dq.append((ny,nx,nd))

print(bfs())