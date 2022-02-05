import sys
from itertools import combinations
input = sys.stdin.readline

p = []
for _ in range(9):
  H = int(input())
  p.append(H)

# height = [int(input()) for _ in range(9)]

combi = list(combinations(p, 7))
for i in combi:

# for combi in combinations(height, 7):

  if sum(i) == 100:
    r = list(i)
    r.sort()
    for j in r:
      print(j)

# height = [int(input()) for _ in range(9)]
# for combi in combinations(height, 7):
#   if sum(combi) == 100:
#     for height in sorted(combi):
#       print(height)

      # =======> 틀린문제 : 100이 되는 수가 많을 수 있으므로 break로 해준다.
      # break
