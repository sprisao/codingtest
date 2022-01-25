import sys

input = sys.stdin.readline
N = int(input())

# 입력 방식 : '999494949' -> 한줄로 입력한다.
num = []

for i in str(N):
    num.append(int(i))
# 따라서 이런식으로 변경해준다.

# 역순 정렬이기 때문에
num.sort(reverse=True)

# 출력되는 방식도 : 999999444 이런식으로 한 줄에 출력되어야한다. 따라서:

for i in num:
    print(i, end='')
