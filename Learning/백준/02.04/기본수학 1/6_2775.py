from multiprocessing.context import ForkContext
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  k = int(input())
  n = int(input())
  p = []
  floor = []
  for i in range(k+1):
    print('ki', i)
    for j in range(1, n+1):
      if i == 0:
        p.append(j)
      else:
        ind = sum(floor[i-1][:j])
        p = p.append(ind)
    floor.append(p)
    print(floor)



# k층 n호
# n호 -> (k-1)층의 1호부터 n 호까지 사람들의 수의 합
# k = 층
# n = 호

# 아파트 0층부터
# 0층의 n호에는 n명이 산다.
# 1층 3호

#    [1][2][3][4][5][6]
# [3] 1  5 15  35 70 126
# [2] 1  4 10  20 35 56 
# [1] 1  3  6  10 15 21
# [0] 1  2  3  4  5  6 
