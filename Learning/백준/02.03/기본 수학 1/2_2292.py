# 1 2-7 8 - 19, 20 - 37, 38-61, 62- 70
# n = 1 6 12 18 24 30 
# n 개수만큼 숫자를 센다 -> n은 6의 등비수열

# [1], [2,3,4,5,6,7], [8,9,10,11,12,13,14,15,16,17,18,19]

# numList = []
# NN = int(input())
# N= 1
# m = 1
# for n in range (5):
#   print(N)
#   midList =[]
#   for _ in range (N):
#     if m == N: 
#       print(N)
#     else:
#       midList.append(m)
#       m = m + 1
#   numList.append(midList)
#   N = 6 * (n+1)

# print(numList)

# N = int(input())
# n = 1
# m = 1
# while True:
#   for i in range(n):
#     if m == N:
#       print(j)ㅈ
#       break
#     else: 
#       m += 1
#     n = 6 * j
#   j += 1

N = int(input())
n = 1
m = 1
while N > m:
  m += 6 * n
  print(m)
  n += 1
print(n)