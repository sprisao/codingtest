
N = int(input())   # 3 <= N <= 10,000
req = list(map(int, input().split())) # 1 <= B[] <= 100,000 
M = int(input()) # N <= M <= 1,000,000,000

lo = 0
hi = max(req)
mid = (lo + hi) // 2
ans = 0

def is_possible(mid):
  ### 이부분이 어려울 수 있다.
    return sum(min(r, mid) for r in req) <= M

while lo <= hi:
  # print(f'lo: {lo}, mid: {mid}, hi: {hi}, ans: {ans}')
  if is_possible(mid):
    lo = mid + 1
    ans = mid 
  else:
    hi = mid - 1
  mid = (lo + hi) // 2

print(ans)