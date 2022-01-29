N = int(input())

# for _ in range(N):
#   a, b = input().split()
#   cnt= int(a)
#   str_list = list(b)
#   for i in str_list:
#     print(i*cnt, end='')

for _ in range(N):
  a, b = input().split()
  for i in b:
    print(i*int(a), end='')
