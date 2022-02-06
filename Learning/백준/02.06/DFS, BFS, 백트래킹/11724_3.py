#방향없는 그래프 -> 인접행렬 -> 대칭
#연결 요소 -> DFS로 훑으면서 새롭게 Check가 추가될때마다 카운팅을한다.

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = list(map(int, input().split()))

adj = [[0] * N for _ in range(N)]
for _ in range(M):
  a, b = map(lambda x: x -1, map(int, input().split()))
  adj[a][b] = adj[b][a] = 1

ans = 0
chk = [False] * N

def dfs(now): 
  for nxt in range(N):
    if adj[now][nxt] and not chk[nxt]:
      chk[nxt] = True
      dfs(nxt)

for i in range(N):
  if not chk[i]: # 이부분[]
    ans += 1
    chk[i] = True  #이부분
    dfs(i)

print(ans)