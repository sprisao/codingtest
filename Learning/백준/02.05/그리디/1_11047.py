# N, K = list(map(int, input().split()))

# cnt = 0
# coins = [int(input()) for _ in range(N)]
# coins.reverse()

# for i in coins:
#   if i < K:
#     cnt += K//i
#     K = (K - (i* (K//i)))
# print(cnt)


N, K = list(map(int, input().split()))

coins = [int(input()) for _ in range(N)]
coins.reverse()

cnt = 0
for i in coins:
    cnt += K//i
    K %= i
print(cnt)