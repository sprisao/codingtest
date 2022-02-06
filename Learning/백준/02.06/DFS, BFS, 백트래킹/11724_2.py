import sys
from time import clock_getres
input = sys.stdin.readline

N, M = list(map(int, input().split()))
adj = [[0]*N for _ in range(N)]

for _ in range(M):
  a, b = map(lambda x: x- 1, map(int,input().split()))
  adj[a][b] = adj[b][a] = 1

# ------------------- 여기까지 굿

ans = 0
#------ 2 번째 -> Check 박스를 만든다.
chk = [False] * N # -> 정점의 개수만큼 체크를 만든다.

print(chk)
# ------------ Clear
def dfs(now):
  for nxt in range(N):
    if adj[now][nxt] and not chk[nxt]:
      chk[nxt] = True
      print('dfs', chk)
      dfs(nxt) 

for i in range(N):
  if not chk[i]:
    ans += 1
    chk[i] = True 
    print('loop',chk)
    dfs(i)

# print(ans)
