import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

ds = set()
for a, b, c, in list(combinations(A,3)):
  r = a + b + c
  if (r <= M):
    ds.add(r) 

print(max(ds))