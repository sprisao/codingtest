# x = kg
# y = cm
# (x, y)
# 
N = int(input())
people = []
for i in range(N):
  A, B = list(map(int, input().split()))
  people.append((A,B))


for person in people:
  cnt = 1
  for others in people:
    if others > person:
      cnt += 1
    else:
      cnt += 0
    
  print(cnt)