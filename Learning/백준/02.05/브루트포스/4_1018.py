# M, N = list(map(int, input().split()))

#10101010 이런 패턴을 가장 많이 나타내는 구간을 먼저 찾고
#그 구간을 포함하는 8*8 범위를 정해 잘나낸뒤
#범위 내에 교차하지 않고 연달아서 같은 색을 나타내는 부분의 수를 찾아 출력한다.


# row = []
# for _ in range(M):
#   row.append(list(input()))

# for line in row:
#   cnt = 0
#   for i in range(0, N-1):
#     if line[i] != line[i+1]:
#       cnt += 1
#   print(cnt)
  # print(cnt-(N-8)-1 if cnt > 0 else cnt-(N-8))

  # 13 - 7 
  # 8

N, M = map(int, input().split())
original = []
count = []

for _ in range(N):
    original.append(input())

for a in range(N-7):
    for b in range(M-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if original[i][j] != 'W':
                        index1 += 1
                    if original[i][j] != 'B':
                        index2 += 1
                else:
                    if original[i][j] != 'B':
                        index1 += 1
                    if original[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))

print(min(count))
