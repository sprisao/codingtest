import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
num = []

for _ in range(N):
    num.append(int(input()))

num.sort()
num_s = Counter(num).most_common()

# 산술평균
print('%d' % round(sum(num)/len(num), 0))

# 중앙값
print(num[N//2])

# 최빈값
if len(num_s) > 1:
    if num_s[0][1] == num_s[1][1]:
        print(num_s[1][0])
    else:
        print(num_s[0][0])
else:
    print(num_s[0][0])

# 범위
print(num[-1] - num[0])

# sum()5
# len()
# '%d' %
# [data].sort()

# 최빈값, 즉 가장 많이 나오는 값을 구하려면 collections의 Counter를 사용하면 된다.
# Counter는 입력된 각각의 값을 'key'로 할당하고, 중복되는 개수가 있을경우 'value'에 추가하여 저장한다. 이후 자동으로 sorted 되어 value가 가장 높은 값이 앞으로 오나보다.
