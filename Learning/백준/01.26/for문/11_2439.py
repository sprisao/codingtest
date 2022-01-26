import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    o = i + 1
    space = N - o
    print('{}'.format(' '*space+'*'*o))
