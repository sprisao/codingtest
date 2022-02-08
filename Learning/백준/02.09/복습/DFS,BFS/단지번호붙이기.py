#정사각형 행렬
# 1 -> 집 있는 곳, 0 -> 집 없는 곳
#좌, 우, 위, 아래로 붙어있는 집 찾기
# 단지수 출력 및 각 단지에 속하는 집의 수를 오름차순으로 정렬

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

board = [int(input()) for _ in range(N)]

dy = [0 , 0, 1, -1]
dx = [-1, 1, 0, 0]


## bfs 길찾기에서 이미 방문한 곳을 어떻게 체크했더라?
chk = [False] * N
def bfs(board, a, b):
  chk[(a,b)] = True
  dq = deque()
  dq.append((a,b))
  while dq:
    x, y = dq.popleft()
    for w in range(4):
      nx = dx + x[w]   ##이부분 [w]를 빼먹었다.
      ny = dy + y[w]   ##이부분도
      if nx < 0 or nx >= n or ny < 0 or ny >=n:
        continue ##이부분도 기억에서 삭제
      # if board[nx][dy] and not chk[(nx,dy)]:
      #   chk[(nx,ny)] = True
      #   dq.append((nx,ny))
      # 이부분 완전히 틀렸다.
      


for a in range(N):
  for b in a:
    if board[a][b] == 1:  ### 이부분
      # chk=[(a,b)]     ## 필요없다.
      bfs(board, a, b)