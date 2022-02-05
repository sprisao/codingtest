import sys
input = sys.stdin.readline

A, B, V = list(map(int, input().split()))

n = (V-B)/(A - B)
print(int(n) if n == int(n) else int(n)+1)