import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
#인풋 속도가 느리다
N, M = list(map(int, input().split()))  

adj =[[0]*N for _ in range(N)]
#인접행렬을 만든다 => 좌표를 만든다.


for _ in range(M):
  a, b = map(lambda x: x - 1, map(int, input().split())) # 보통 정점의 개수 0 < N 으로 시작 하지만 여기선 1 < N으로 시작했기 때문에 1을 빼줘야 한다고 함 
  adj[a][b] = adj[b][a] = 1
  # 양방향이기 때문에 반대로도 찍어준다.
#좌표에 값을 찍어준다.


# for row in adj:
#   print(row)


ans = 0 
chk = [False] * N
#체크포인트는 6개여야 한다. 

# dfs 함수를 만들어준다.
def dfs(now):
  for nxt in range(N):
    if adj[now][nxt] and not chk[nxt]:
      chk[nxt] = True
      dfs(nxt)

for i in range(N):
  if not chk[i]:
    ans += 1
    chk[i] = True 
    dfs(i)

print(ans)

#무방향 그래프
#연결요소를 구해라

#1. 테스트 케이스 분석
#2. 인접행렬을 쓸것인가 아니면 인접리스트를 쓸것인가?
# 1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2 <-- 이런식으로 주어진 이유는?
#3. O(N2)에 육박하기 때문에 인접행렬 사용
# 4. 인접행렬과 BFS를 활용하여 풀이
# lambda의 사용법