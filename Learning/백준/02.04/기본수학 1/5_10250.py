# 같은 호수면 아래층 방을 선호한e다 

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  H, W, N = list(map(int, input().split()))
  yy = 1
  xx = 1
  n = 1
  for i in range(N):
    r = yy*100 + xx
    if yy < H:
      yy += 1
    else:
      yy = 1
      xx += 1
  print(r)