import sys
input = sys.stdin.readline

N = int(input())

r = []
# for num in range(N):
#   num_list= []
#   for i in str(num):
#     num_list.append(int(i))
#     if num + sum(num_list) == N:
#       r.append(num)
#       break
# if len(r) == 0:
#   print('0')
# else:
#   print(r[0])

import sys
input = sys.stdin.readline

N = int(input())

r = []
num = 1
while num < N:
  num_list = [int(i) for i in str(num)]
  if num + sum(num_list) == N: 
    r.append(num)
    break
  num += 1

print(r[0] if len(r) != 0 else '0')