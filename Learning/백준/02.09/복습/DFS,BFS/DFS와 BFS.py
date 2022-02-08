# 정점번호가 작은 것부터 먼저 방문하라.
# 더 이상 방문할 수 있는 점이 없는 경우 종료하라.
# 정점 번호는 1번부터 N번까지다.
# 간선은 양방향
# 1 <= n <= 1,000 정점의 개수 
# 1 <= m <= 10,000 간선의 개수
# v 시작지점

from collections import deque
import sys
input = sys.stdin.readline

n, m, v = list(map(int,input().split()))

#인접 행렬 만들기

adj= [[0] * n for _ in range(n)]

for _ in range(m):
  a, b = map(lambda x: x -1, map(int, input().split()))
  adj[a][b] = adj[b][a] = 1

# for row in adj:
#   print(row)


# 깊이 우선 탐색 DFS
chk = [False] * n    ### 간곳 췌크하는 놈 [False] * n 만으로 체크가 가능하다는 점이 100% 이해되진 않는다.
def dfs(now):        #dfs가 (now)값을 받아온다.
  chk[now]=True      #받아온 now는 일단 시작한 지점이라고 체크를 해준다.
  print(now +1, end=' ')    # 출력값은 리스트 제작을 위해 -1 을 해준 부분을 다시 +1 하여 출력한다. 이 것은 방문된 점이다.
  for nxt in range(n):
    if adj[now][nxt] and not chk[nxt]:
      chk[nxt] = True
      dfs(nxt)

dfs(v-1)   ### 1. dfs에 시작점을 준다. 첫번째 열부터 값이 들어가도록 인접행렬을 만들었기 때문에 첫째열을 1로 인식해야한다. 따라서 시작점에서 -1을 해준다.  -> 문제에 따라 시작점이 다를 수 있고, for 문을 통해서 시작점을 탐색해야 될 수도 있다.



### 넓이 우선 탐색 BFS

bfsChk = [False]*n  ## DFS와 BFS로 동시에 풀이해야 하기 때문에 chk를 두개 만들어 주엇어야 한다.
def bfs(start):
  bfsChk[start] = True
  dq = deque()          #BFS는 deque를 사용하기 때문에 dq를 deque로 정의해주고
  dq.append(start)        #현재값을 일단 dq안에 넣어준다.
  while dq:             #dq 안에 값이 있을경우 while문이 돌아가는데
    now = dq.popleft()    #일단 dq에 들어간 값을 먼저 빼주고
    print(now + 1, end=' ')
    for nxt in range(n):  #해당 x 값, 즉 현재값에서
      # print(nxt)
      # print(bfsChk[nxt])
      if adj[now][nxt] and not bfsChk[nxt]: #다음 움직일 수 잇는 무브먼트의 경우의 수를 살펴보고 가보지 않은 곳이면 
        bfsChk[nxt] = True      # 들어가서 들어갔다고 체크한다.
        dq.append(nxt)          # 해당 값을 다시 dq에 넣어준다.
                                # DFs에서는 마지막에 'nxt' 값을 토대로 dfs(nxt)를 돌리지만 bfs에서는 while 문 안에서 해결한다.
                                # 이후 새로운 
print()
bfs(v-1)