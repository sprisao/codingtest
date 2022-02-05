

# 1번째  [2번째], [3번째], [4번째 ]  num
# [1개]  [2개], [3개], [4개]  num
#  1개   3개    6개   10개  num_count

# # # 1, [1, 2], [3, 2, 1], [1, 2, 3, 4], [5, 4, 3, 2, 1,]
# 1, [2, 1], [1, 2, 3], [4, 3, 2, 1], [1, 2, 3, 4, 5,]

x = int(input())
num_list = []

num = 0
num_count = 0

while num_count < x:
    num += 1
    print('num',num)
    num_count += num
    print('num_count',num_count)


num_count -= num #이게왜????????????
print('num_count', num_count)

if num % 2 == 0:
    i = x - num_count
    print('분자', i)
    j = num - i + 1
    print('분모',j)
else:
    i = num - (x - num_count) + 1
    print(i)
    j = x - num_count
    print(j)

print(f"{i}/{j}")