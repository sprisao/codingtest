N = int(input())

mb = []
for _ in range(N):
    a, b = input().split()
    a = int(a)
    b = str(b)
    mb.append((a, b))

# 이부분이 좀 희안하네 lambda를 활용해서 sorting하는 부분을 다시한번 봐야겄다.

mb.sort(key=lambda b: (b[0]))

for a, b in mb:
    print(a, b)
