import sys
input = sys.stdin.readline

N = int(input())

num = N
for i in range(N):
    num = num - 1
    print(num+1)
