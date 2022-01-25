import sys

input = sys.stdin.readline
N = int(input())

#빠른 입출력!!

num =[]
for _ in range(N):
 num.append(int(input()))

num.sort()

for i in num:
 print(i)
