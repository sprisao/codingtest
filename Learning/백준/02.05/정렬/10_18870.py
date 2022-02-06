N = int(input())
nums = list(map(int,input().split()))

arr = list(sorted(set(nums)))

d = {arr[i]:i for i in range(len(arr))}

for i in nums:
  print(d[i], end=' ')
