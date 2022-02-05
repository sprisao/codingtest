import sys
input = sys.stdin.readline

A, B, C = list(map(int, input().split()))

if B >= C: 
  print('-1')
else:
  print(int(A/(C-B)+1))
  
# n = 1
# while True:
#   expense = A + (B*n)
#   earning = C * n
#   n = n + 1
#   if expense <= earning:
#     print(n)
#     break